from json import JSONEncoder
from django.http import JsonResponse
from ninja import Router
from api.models.users import User
from api.schemas.users import UserSchemaIn, UserSchemaOut

router = Router(tags="user")


@router.post("/")
def create_user(request, new_user=UserSchemaIn):
    _user = User.objects.create(username=new_user.username, password=new_user.password)
    _user.save()
    return JsonResponse(content=JSONEncoder(_user.dict()), status_code=201)
