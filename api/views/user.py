from typing import List
from ninja import Router
from api.models.users import User
from api.schemas.users import UserSchemaIn, UserSchemaOut

router = Router(tags=["user"])

# DELETE THIS BEFORE PROD
@router.post("/", response=UserSchemaOut)
def create_user(request, new_user: UserSchemaIn, auth=None):
    _user = User.objects.create(username=new_user.username, password=new_user.password)
    _user.save()
    return _user


@router.get("/", response=List[UserSchemaOut])
def get_all_users(request):
    return User.objects.all()
