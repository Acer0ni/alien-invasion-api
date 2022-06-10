from ninja import ModelSchema
from api.models.score import Score


class ScoreSchemaIn(ModelSchema):
    class Config:
        model = Score
        model_fields = ["score", "user"]


class ScoreSchemaOut(ModelSchema):
    class Config:
        model = Score
        model_fields = ["id", "score", "user"]
