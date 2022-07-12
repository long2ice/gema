from gema.dest.go import Go
from gema.dest.pydantic import Pydantic
from gema.dest.rust import Rust
from gema.enums import DestType, Language, SourceType
from gema.source.json import Json
from gema.source.xml import Xml
from gema.utils import camel_to_snake, get_dest_cls, get_source_cls


def test_camel_to_snake():
    assert camel_to_snake("camel2_camel2_case") == "camel2_camel2_case"
    assert camel_to_snake("getHTTPResponseCode") == "get_http_response_code"
    assert camel_to_snake("HTTPResponseCodeXYZ") == "http_response_code_xyz"


def test_get_source_cls():
    assert get_source_cls(SourceType.json) is Json
    assert get_source_cls(SourceType.xml) is Xml


def test_get_dest_cls():
    assert get_dest_cls(Language.rust, DestType.rust) is Rust
    assert get_dest_cls(Language.go, DestType.go) is Go
    assert get_dest_cls(Language.python, DestType.pydantic) is Pydantic
