from typing import Optional

import typer

from gema.enums import DestType, SourceType
from gema.utils import get_dest_cls, get_source_cls


def main(
    source: Optional[str] = typer.Option(None, "-s", "--source", help="Source content"),
    source_file: Optional[typer.FileText] = typer.Option(
        None, "-f", "--source-file", help="Source file"
    ),
    source_type: SourceType = typer.Option(
        SourceType.json, "--source-type", help="Source content type"
    ),
    dest_file: Optional[str] = typer.Option(
        None,
        "-d",
        "--dest-file",
        help="Destination file, will to display in stdout if is not present",
    ),
    dest_type: DestType = typer.Option(..., "--dest-type", help="Destination content type"),
    optional: bool = False,
    snake_case: bool = False,
):
    content = source
    if source_file:
        content = source_file.read()
    source_cls = get_source_cls(source_type)
    sb = source_cls(content)
    decoded = sb.decode()
    dest_cls = get_dest_cls(dest_type)
    db = dest_cls(sb.get_model(decoded), optional=optional, snake_case=snake_case)
    result = db.render()
    if dest_file:
        with open(dest_file, "w") as f:
            f.write(result)
    else:
        typer.echo(result)


if __name__ == "__main__":
    typer.run(main)
