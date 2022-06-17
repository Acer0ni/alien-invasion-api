from ninja import Router
from ninja.errors import HttpError
from django.contrib.auth import login, logout, authenticate
from api.schemas.auth import loginSchema
from api.schemas.users import UserSchemaIn, UserSchemaOut
from api.models.users import User


router = Router(tags=["auth"])


@router.post("/register", response=UserSchemaOut, auth=None)
def register_user(request, incoming_user: UserSchemaIn):
    new_user = User.objects.create(**incoming_user.dict())
    new_user.set_password(incoming_user.password)
    new_user.save()
    login(request, new_user)
    return new_user


@router.post("/login", response=UserSchemaOut, auth=None)
def user_login(request, data: loginSchema):
    logged_in_user = authenticate(
        request, username=data.username, password=data.usernames
    )
    if logged_in_user is not None:
        login(request, logged_in_user)
        return logged_in_user
    raise HttpError(403, "invalid credentials")
