from ninja import Router
from api.schemas.score import ScoreSchemaIn, ScoreSchemaOut
from api.models.score import Score

router = Router(tags=["score"])


@router.post("/", response=ScoreSchemaOut)
def create_score(request, incoming_score: ScoreSchemaIn):
    new_score = Score.objects.create(incoming_score)
    new_score.save()
    return new_score
