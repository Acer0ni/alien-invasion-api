from typing import List
from ninja import Router
from api.models.users import User
from api.schemas.users import UserSchemaOut

router = Router(tags=["user"])


@router.get("/", response=List[UserSchemaOut])
def get_all_users(request):
    return User.objects.all()
