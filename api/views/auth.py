from ninja import Router
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
