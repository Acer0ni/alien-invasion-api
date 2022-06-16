from ninja import Schema


class loginSchema(Schema):
    username: str
    password: str
