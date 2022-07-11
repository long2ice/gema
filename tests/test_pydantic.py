from gema.dest.pydantic import Pydantic
from gema.source.json import Json

content = """{"foo": 5, "barBaz": "hello"}"""
j = Json(content)
model = j.get_model(j.decode())


def test_json():
    dest = Pydantic(model)
    assert (
        dest.render()
        == """from pydantic import BaseModel


class Model(BaseModel):
    foo: int
    barBaz: str

"""
    )


def test_json_snake_case():
    dest = Pydantic(model, snake_case=True)
    assert (
        dest.render()
        == """from pydantic import BaseModel
from pydantic import Field


class Model(BaseModel):
    foo: int
    bar_baz: str = Field(..., alias='barBaz')

"""
    )


def test_json_optional():
    dest = Pydantic(model, optional=True)
    assert (
        dest.render()
        == """from pydantic import BaseModel
from typing import Optional


class Model(BaseModel):
    foo: Optional[int]
    barBaz: Optional[str]

"""
    )


def test_json_optional_and_snake_case():
    dest = Pydantic(model, optional=True, snake_case=True)
    assert (
        dest.render()
        == """from pydantic import BaseModel
from pydantic import Field
from typing import Optional


class Model(BaseModel):
    foo: Optional[int]
    bar_baz: Optional[str] = Field(..., alias='barBaz')

"""
    )


def test_json_nest():
    nest_content = """{
  "foo": 5,
  "barBaz": "hello",
  "nest": {
    "foo": 5,
    "barBaz": "hello"
  },
  "nests": [
    {
      "foo": 5,
      "barBaz": "hello",
      "nest": {
        "foo": 5,
        "barBaz": "hello"
      }
    }
  ]
}

"""
    jn = Json(nest_content)
    dest = Pydantic(jn.get_model(jn.decode()))
    assert (
        dest.render()
        == """from pydantic import BaseModel
from typing import List


class Nest(BaseModel):
    foo: int
    barBaz: str


class Nests(BaseModel):
    foo: int
    barBaz: str
    nest: 'Nest'


class Model(BaseModel):
    foo: int
    barBaz: str
    nest: 'Nest'
    nests: List['Nests']

"""
    )
