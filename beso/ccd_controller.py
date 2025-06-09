import asyncio
import logging
#import aiohttp
from typing import Optional

from beso.ccd_state import CcdState
from beso.settings import Settings

logger = logging.getLogger('ccd')

class CCDController:
    """
    A controller for the BESO CCD camera.
    This class is responsible for managing the CCD camera's settings and operations.
    """

    def __init__(self, settings: Settings):
        self.settings = settings
        self.ccd_state: Optional[CcdState] = None
        self.connection = None

    def is_connected(self) -> bool:
        """
        Check if the CCD camera is connected.
        :return: True if connected, False otherwise.
        """
        return self.connection is not None and self.connection.is_connected()

    async def connect(self) -> None:
        """
        Connects to the BESO camera server via TCP socket using the INET protocol.
        Retrieves CCD state and initializes the connection.
        """
        host = self.settings.beso_host
        port = self.settings.beso_port

        try:
            reader, writer = await asyncio.open_connection(host, port)
            self.connection = (reader, writer)
            logger.info(f"TCP connection to BESO at {host}:{port} established")

            # Send IDENTIFY command
            response = await self._send_command("IDENTIFY CAMERA")
            if response:
                logger.info(f"Camera {response.decode().strip()} connected successfully.")
                self.ccd_state = CcdState(is_exposing=False, exposure_time=0.0)
            else:
                logger.warning("No response received from IDENTIFY CAMERA command.")

        except Exception as e:
            logger.error(f"Failed to connect to BESO camera server: {e}")
            self.connection = None

    async def close(self) -> None:
        """
        Close the connection to the CCD camera.
        """
        if self.connection:
            reader, writer = self.connection
            writer.close()
            await writer.wait_closed()
            self.connection = None
            logger.info("Connection to BESO camera closed.")


    async def set_temperature(self, temperature: float) -> None:
        """
        Example command: Set the target temperature of the CCD camera.

        :param temperature: Desired temperature in Celsius.
        """
        command = f"SET TEMP {temperature:.1f}"
        response = await self._send_command(command)
        logger.info(f"Set temperature response: {response.decode().strip()}")

    async def _write(self, payload: bytes) -> None:
        """
        Write a command to the CCD camera.
        :param payload: The command to send.
        """
        if self.connection is None:
            raise RuntimeError("Not connected to the CCD camera.")

        reader, writer = self.connection
        writer.write(payload)
        await writer.drain()
        logger.debug(f"Sent command: {payload.decode().strip()}")

    async def _read(self) -> bytes:
        """
        Read a response from the CCD camera.
        :return: The response from the camera.
        """
        if self.connection is None:
            raise RuntimeError("Not connected to the CCD camera.")

        reader, _ = self.connection
        response = await reader.readline()
        logger.debug(f"Received response: {response.decode().strip()}")
        return response

    async def _send_command(self, command: str) -> bytes:
        """
        Send a command to the CCD camera and return the response.
        :param command: The command to send.
        :return: The response from the camera.
        """
        await self._write(command.encode() + b'\n')
        return await self._read()






