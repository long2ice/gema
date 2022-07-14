from enum import Enum


class SourceType(str, Enum):
    json = "json"
    xml = "xml"
    yaml = "yaml"


class DestType(str, Enum):
    pydantic = "pydantic"
    go = "go"
    rust = "rust"
    dataclass = "dataclass"
    typescript = "typescript"


class Language(str, Enum):
    python = "python"
    go = "go"
    rust = "rust"
    typescript = "typescript"
