from dataclasses import dataclass

@dataclass
class FitsMetadata:
    """Metadata for FITS files.

    This class is used to store metadata for FITS files, which is passed to BESO.
    Those data will be added to the FITS header.
    The intention is to provide BESO with all the data it does not have in possession.
    """
    object_name: str
    ra: float
    dec: float
    alt: float
    az: float

@dataclass
class ExposureMetadata:
    """Metadata for BESO.

    This class is used to store metadata for BESO, which is passed to the BESO.
    """
    filename: str
    fits_metadata: FitsMetadata
