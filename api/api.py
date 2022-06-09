from ninja import NinjaAPI

api = NinjaAPI(
    title="score tracker!",
    description="an api to keep track of alien invasions highscores",
    version="0.0.0",
    auth=None,
    csrf=True,
)

from api.views.user import router as user_router


api.add_router("highscore", user_router)
