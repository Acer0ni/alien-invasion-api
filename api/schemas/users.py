from ninja import ModelSchema
from models.users import User


class UserSchemaIn(ModelSchema):
    class config:
        model = User
        model_fields = {"username", "password"}


class UserSchemaOut(ModelSchema):
    class config:
        model = User
        model_fields = ["id", "username"]
