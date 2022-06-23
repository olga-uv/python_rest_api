from typing import Optional
from pydantic import BaseModel, ValidationError


class Positions(BaseModel):
    position_name: str
    position_id: int


class User(BaseModel):
    user_name: str
    user_id: int
    age: int
    some_stuff: Optional[int]
    positions: list[Positions]


response = '{"user_name": "Yoda", "user_id": "8989", "some_stuff": "e43234", "age": "1027", ' \
           '"positions": [{"position_name": "Jedi Master", "position_id": "123"}]}'


try:
    user = User.parse_raw(response)
    print(user)
except ValidationError as e:
    error = e.json()
    print(error)


