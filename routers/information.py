from fastapi import APIRouter

router = APIRouter(
    prefix='/informations',
    tags=['Informations']
)


@router.get('/moreInformation')
def moreInformation():
    return {"message": "Aucune info"}
