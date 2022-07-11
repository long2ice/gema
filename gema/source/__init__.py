from typing import Any, Union

from gema import Base
from gema.enums import SourceType
from gema.schema import Field, Model


class Source(Base):
    type: SourceType

    def __init__(self, content: str):
        self.content = content

    def decode(self):
        raise NotImplementedError

    def get_model(self, content: Union[list, dict]) -> Model:
        model = Model(fields=[])
        if isinstance(content, list):
            item = content[0]
        else:
            item = content
        for k, v in item.items():
            if isinstance(v, dict):
                field = Field(name=k, type=self.get_model(v))
            elif isinstance(v, list):
                if isinstance(v[0], dict):
                    field = Field(name=k, type=[self.get_model(v)])
                else:
                    field = Field(name=k, type=[type(v[0])])
            elif v is None:
                field = Field(name=k, type=Any)
            else:
                field = Field(name=k, type=type(v))
            model.fields.append(field)
        return model
