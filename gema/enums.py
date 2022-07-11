from enum import Enum


class SourceType(str, Enum):
    json = "json"
    xml = "xml"


class DestType(str, Enum):
    pydantic = "pydantic"
    go = "go"
    rust = "rust"
