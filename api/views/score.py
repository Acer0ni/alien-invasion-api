from typing import List
from django.http import HttpRequest

from ninja import Router
from api.schemas.score import ScoreSchemaIn, ScoreSchemaOut
from api.models.score import Score
from api.models.users import User

router = Router(tags=["score"])


@router.post("/", response=ScoreSchemaOut)
def create_score(request: HttpRequest, incoming_score: ScoreSchemaIn) -> Score:
    current_highscore: Score = Score.objects.order_by("-score").first()
    new_score = create_score_object(request, incoming_score)
    if current_highscore.score > new_score.score:
        return current_highscore
    else:
        return new_score


# move this to own file
def check_for_highscore(current_highscore: Score, incoming_score: Score) -> bool:
    if not current_highscore or incoming_score.score > current_highscore.score:
        return True
    return False


def create_score_object(request: HttpRequest, incoming_score: ScoreSchemaIn) -> Score:
    user: User = User.objects.get(id=request.user.id)
    new_score = Score.objects.create(score=incoming_score.score, user=user)
    new_score.save()
    return new_score


@router.get("/", response=List[ScoreSchemaOut])
def get_scores(request) -> List[Score]:
    return Score.objects.all()


@router.get("/highscore", response=ScoreSchemaOut, auth=None)
def get_highscore(request):
    return Score.objects.all().order_by("-score").first()
