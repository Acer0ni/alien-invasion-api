from ninja import NinjaAPI
from ninja.security import django_auth

api = NinjaAPI(
    title="score tracker!",
    description="an api to keep track of alien invasions highscores",
    version="0.0.0",
    auth=django_auth,
    csrf=True,
)

from api.views.user import router as user_router
from api.views.score import router as score_router
from api.views.auth import router as auth_router

api.add_router("auth", auth_router)
api.add_router("user", user_router)
api.add_router("score", score_router)
