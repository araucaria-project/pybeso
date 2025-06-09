import argparse
import asyncio
import logging
from beso.settings import Settings
from beso.ccd_controller import CCDController

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("beso")

async def main():
    parser = argparse.ArgumentParser(prog="beso", description="BESO CCD Controller CLI")
    subparsers = parser.add_subparsers(dest="command")

    ccd_parser = subparsers.add_parser("ccd", help="Control CCD camera")
    ccd_subparsers = ccd_parser.add_subparsers(dest="ccd_command")

    # Subcommand: temperature-set
    temp_set_parser = ccd_subparsers.add_parser("temperature-set", help="Set CCD temperature")
    temp_set_parser.add_argument("temperature", type=float, help="Target temperature in Celsius")
    temp_set_parser.add_argument("--verbose", action="store_true", help="Verbose output")

    # Subcommand: state
    ccd_subparsers.add_parser("state", help="Print CCD state")

    args = parser.parse_args()

    if args.command == "ccd":
        settings = Settings()  # Zakładamy domyślną konfigurację
        controller = CCDController(settings)
        await controller.connect()

        if args.ccd_command == "temperature-set":
            await controller.set_temperature(args.temperature)
            if args.verbose:
                logger.info("Temperature set command sent.")

        elif args.ccd_command == "state":
            if controller.ccd_state:
                print(controller.ccd_state)
            else:
                print("No CCD state available.")

        await controller.close()
    else:
        parser.print_help()

if __name__ == "__main__":
    asyncio.run(main())