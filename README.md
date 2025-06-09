# pybeso

Asynchronous Python CLI and controller library for the BESO CCD camera.

Provides tools to connect to the BESO CCD server over TCP and issue commands via a simple command-line interface.

## 🔧 Installation

1. Clone this repository:
   ```bash
    git clone https://github.com/araucaria-project/pybeso.git
    cd pybeso
   ```

2. Install in editable mode:
    ```bash
    pip install -e .
    ```

   Or build:
    ```bash
    pip install build
    python -m build
    ```

## icon:  Use as a library
You can use the `beso` library to control the CCD camera programmatically:

```python
from beso.ccd_controller import CcdController, Settings
async def main():
    settings = Settings(host='beso.example.com', port=30020)
    controller = CcdController(settings)
    
    await controller.connect()
    #...
```

## 🚀 Usage as CLI

You can use the `beso` CLI tool to control the CCD camera:

### Set temperature
```bash
   beso ccd temperature-set -40.0 --verbose
```
    
### Check current CCD state
```bash
    beso ccd state
```
## 🧠 Project structure

- `main.py` – CLI entrypoint
- `ccd_controller.py` – Asynchronous TCP controller for the BESO camera
- `settings.py` – Configuration data (host, port)
- `pyproject.toml` – Project metadata and scripts

## 🧪 Example output
```bash
    $ beso ccd temperature-set -40 --verbose
    INFO:beso:Connected to BESO camera at 192.168.0.101:30020
    INFO:beso:Set temperature response: OK

    $ beso ccd state
    is_exposing=False 
    exposure_time=0.0

```

## 🛠 Requirements

- Python 3.11+
- No external dependencies (yet 😈)