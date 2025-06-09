# pybeso

Asynchronous Python CLI and controller library for the BESO CCD camera.

Provides tools to connect to the BESO CCD server over TCP and issue commands via a simple command-line interface.

## 🔧 Installation

1. Clone this repository:
    git clone https://your.repo/pybeso.git
    cd pybeso

2. Install in editable mode:
    pip install -e .

   Or build:
    pip install build
    python -m build

## 🚀 Usage

You can use the `beso` CLI tool to control the CCD camera:

### Set temperature
    beso ccd temperature-set -40.0 --verbose

### Check current CCD state
    beso ccd state

## 🧠 Project structure

- `main.py` – CLI entrypoint
- `ccd_controller.py` – Asynchronous TCP controller for the BESO camera
- `settings.py` – Configuration data (host, port)
- `pyproject.toml` – Project metadata and scripts

## 🧪 Example output

    $ beso ccd temperature-set -40 --verbose
    INFO:beso:Connected to BESO camera at 192.168.0.101:30020
    INFO:beso:Set temperature response: OK

    $ beso ccd state
    CcdState(is_exposing=False, exposure_time=0.0)

## 🔄 Interactive mode (planned)

Future versions may support an interactive mode:

    beso ccd
    BESO CCD: temperature
    -39.8
    BESO CCD: _

## 🛠 Requirements

- Python 3.8+
- No external dependencies beyond `argparse` and `asyncio` (standard library)