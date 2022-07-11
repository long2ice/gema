from gema.dest import Dest
from gema.enums import DestType


class Rust(Dest):
    template_file = "pydantic.jinja2"
    type = DestType.rust
