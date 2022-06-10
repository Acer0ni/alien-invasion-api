from ninja import NinjaAPI

api = NinjaAPI(
    title="score tracker!",
    description="an api to keep track of alien invasions highscores",
    version="0.0.0",
    auth=None,
    csrf=True,
)

from api.views.user import router as user_router
from api.views.score import router as score_router

api.add_router("user", user_router)
api.add_router("score", score_router)
