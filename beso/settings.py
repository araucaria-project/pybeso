from dataclasses import dataclass


@dataclass
class Settings:
    beso_host: str
    beso_port: int