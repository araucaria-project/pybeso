
from dataclasses import dataclass

@dataclass
class CcdState:
    """The state of the CCD camera.

    This is to keep, redundantly, the state and setup of the BESO CCD camera.
    """
    is_exposing: bool
    exposure_time: float
    # add more fields as needed (binning, gain etc...)

