from jinja2 import Environment, FileSystemLoader, select_autoescape

from gema import Base
from gema.enums import DestType, Language
from gema.schema import Model

env = Environment(loader=FileSystemLoader("gema/dest/templates"), autoescape=select_autoescape())


class Dest(Base):
    template_file: str
    type: DestType
    language: Language

    def __init__(self, model: Model, **kwargs):
        self.model = model
        self.template = env.get_template(self.template_file)

    def render(self):
        return self.template.render(model=self.model)
