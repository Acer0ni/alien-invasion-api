from django.http import JsonResponse
from ninja import Router
from ninja.errors import HttpError
from django.contrib.auth import login, logout, authenticate
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
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
        request, username=data.username, password=data.password
    )
    if not logged_in_user:
        raise HttpError(403, "invalid credentials")
    login(request, logged_in_user)
    return logged_in_user


@router.post("/logout")
def user_logout(request):
    logout(request)
    return {"msg": "you have logged out succesfully"}


@router.get("/csrf", auth=None)
@ensure_csrf_cookie
def get_csrf(request):
    return JsonResponse({"msg": "it works"})
