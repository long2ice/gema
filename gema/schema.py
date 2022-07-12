from typing import List, Optional, Type, Union

from pydantic import BaseModel
from pydantic import Field as PydanticField

from gema.enums import DestType, Language, SourceType


class ConvertReq(BaseModel):
    source_type: SourceType = PydanticField(SourceType.json)
    content: str = PydanticField(..., example='{"a": 1}')
    language: Language = PydanticField(..., example=Language.python)
    dest_type: DestType = PydanticField(..., example=DestType.pydantic)
    config: Optional[dict]


class ConvertRes(BaseModel):
    content: str


class Field(BaseModel):
    name: str
    type: Union[Type, "Model", List["Model"], List["Type"]]


class Model(BaseModel):
    fields: List[Field]


Field.update_forward_refs()
