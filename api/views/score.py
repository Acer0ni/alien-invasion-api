from typing import List
from ninja import Router
from api.schemas.score import ScoreSchemaIn, ScoreSchemaOut
from api.models.score import Score
from api.models.users import User

router = Router(tags=["score"])

# todo rename the create functions
@router.post("/", response=ScoreSchemaOut)
def create_score(request, incoming_score: ScoreSchemaIn):
    current_highscore = Score.objects.order_by("-score").first()
    new_score = create_score_object(request, incoming_score)
    if current_highscore.score > new_score.score:
        return current_highscore
    else:
        return new_score


# move this to own file
def check_for_highscore(current_highscore, incoming_score):
    if not current_highscore or incoming_score > current_highscore:
        return True
    return False


def create_score_object(request, incoming_score: ScoreSchemaIn):
    user = User.objects.get(id=incoming_score.user)
    new_score = Score.objects.create(score=incoming_score.score, user=user)
    new_score.save()
    return new_score


@router.get("/", response=List[ScoreSchemaOut])
def get_scores(request):
    return Score.objects.all()


@router.get("/highscore", response=ScoreSchemaOut, auth=None)
def get_highscore(request):
    return Score.objects.all().order_by("-score").first()
