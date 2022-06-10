from ninja import ModelSchema
from api.models.users import User


class UserSchemaIn(ModelSchema):
    class Config:
        model = User
        model_fields = {"username", "password"}


class UserSchemaOut(ModelSchema):
    class Config:
        model = User
        model_fields = ["id", "username"]
