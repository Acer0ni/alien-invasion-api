from ninja import ModelSchema
from models.highscore import Highscore


class HighscoreSchemaIn(ModelSchema):
    class config:
        model = Highscore
        model_fields = ["score", "user"]


class HighscoreSchemaOut(ModelSchema):
    class config:
        model = Highscore
        model_fields = ["id", "score", "user.username"]
