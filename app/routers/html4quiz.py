from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.dependencies import get_db
from app.models import QG
# from sqlalchemy import func
# from app.schemas import QgsCategoryOnly
from app.makeHTML import MakeHTML

router = APIRouter()

@router.get("/qg_preview/{qg_id}")
def preview_qg(qg_id: int, db: Session = Depends(get_db)):
    qg = db.query(QG).get(qg_id)
    try:
        qg_dict = {'category': qg.category,
                   'kind': qg.kind,
                   'name': qg.name,
                   'questions': qg.questions,
                   'answers': qg.answers}
        MakeHTML(qg_dict)
        return {'message': 'QG preview is successful'}
    except Exception as e:
        return {"error": f"Failed with {e}"}

