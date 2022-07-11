from typing import List, Type, Union

from pydantic import BaseModel


class Field(BaseModel):
    name: str
    type: Union[Type, "Model", List["Model"], List["Type"]]


class Model(BaseModel):
    fields: List[Field]


Field.update_forward_refs()
