from ninja import ModelSchema, Schema
from api.models.users import User


class UserSchemaIn(ModelSchema):
    class Config:
        model = User
        model_fields = {"username", "password"}


class UserSchemaOut(Schema):
    id: int
    username: str
