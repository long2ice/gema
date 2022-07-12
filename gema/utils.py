import importlib
import inspect
import pkgutil
import re

from gema import dest, source
from gema.dest import Dest
from gema.enums import DestType, Language, SourceType
from gema.source import Source


def camel_to_snake(name):
    name = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", name)
    return re.sub("([a-z0-9])([A-Z])", r"\1_\2", name).lower()


def _discover_source_type():
    ret = {}
    for m in pkgutil.iter_modules(source.__path__):
        mod = importlib.import_module(f"{source.__name__}.{m.name}")
        for name, member in inspect.getmembers(mod, inspect.isclass):
            if issubclass(member, Source) and member is not Source:
                ret[member.type] = member
    return ret


def _discover_dest_type():
    ret = {}
    for m in pkgutil.iter_modules(dest.__path__):
        mod = importlib.import_module(f"{dest.__name__}.{m.name}")
        for name, member in inspect.getmembers(mod, inspect.isclass):
            if issubclass(member, Dest) and member is not Dest:
                ret.setdefault(member.language, {})[member.type] = member
    return ret


_source_cls_map = _discover_source_type()
_dest_cls_map = _discover_dest_type()


def get_source_cls(type_: SourceType):
    return _source_cls_map[type_]


def get_dest_cls(language: Language, type_: DestType):
    return _dest_cls_map[language][type_]
