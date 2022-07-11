import importlib
import inspect
import pkgutil
import re
from types import ModuleType
from typing import Type

from gema import Base, dest, source
from gema.dest import Dest
from gema.enums import DestType, SourceType
from gema.source import Source


def camel_to_snake(name):
    name = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", name)
    return re.sub("([a-z0-9])([A-Z])", r"\1_\2", name).lower()


def _discover_type(module: ModuleType, cls: Type[Base]):
    ret = {}
    for m in pkgutil.iter_modules(module.__path__):
        mod = importlib.import_module(f"{module.__name__}.{m.name}")
        for name, member in inspect.getmembers(mod, inspect.isclass):
            if issubclass(member, cls) and member is not cls:
                ret[member.type] = member
    return ret


_source_cls_map = _discover_type(source, Source)
_dest_cls_map = _discover_type(dest, Dest)


def get_source_cls(type_: SourceType):
    return _source_cls_map[type_]


def get_dest_cls(type_: DestType):
    return _dest_cls_map[type_]
