from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.dependencies import get_db
from app.models import QG
from app.schemas import QgsCategoryOnly

router = APIRouter()

@router.get("/qgs", response_model=list[QgsCategoryOnly])
def get_qgs(db: Session = Depends(get_db)):
    results = (
        db.query(
            func.min(QG.id).label("id"),  # 대표 ID 선택
            QG.category.label("category"),  # 카테고리 이름
            func.count(QG.category).label("count")  # 동일 카테고리 갯수
        )
        .group_by(QG.category)
        .order_by("id")  # 💡 계산된 대표 'id'의 오름차순(asc)으로 정렬합니다
        .all()
    )

    # 2. SQLAlchemy가 반환한 Row 객체들을 Pydantic 모델이 읽을 수 있도록 변환하여 반환합니다.
    return results


@router.get("/qgs/{qg_category}")
def get_qg(qg_category: str, db: Session = Depends(get_db)):
    # return db.query(QG).get(qg_id)
    qgs_list = (
        db.query(QG)
        .filter(
            QG.category == qg_category
        )
        .all()
    )
    return qgs_list


@router.get("/qgs_name/{qg_name}")
def get_qg(qg_name: str, db: Session = Depends(get_db)):
    qg = (
        db.query(QG)
        .filter(
            QG.name == qg_name
        )
        .first()
    )

    return qg


@router.post("/qgs")
def create_qg(qg: dict, db: Session = Depends(get_db)):
    db_qg = (
        db.query(QG)
        .filter(
            QG.name == qg["name"],
            QG.author == qg['author']
        )
        .first()
    )

    if db_qg is None:
        db_qg = QG(
            category=qg["category"],
            author=qg["author"],
            created=qg["created"],
            kind=qg["kind"], # short/choices/action
            name=qg["name"],
            description=qg["description"],
            questions = [f.strip() for f in qg["questions"].split(",")],
            answers = qg["answers"],
            used = []
        )
        db.add(db_qg)
        db.commit()
        db.refresh(db_qg)
        return {'message': 'QG created'}
    else:
        db_qg.category = qg["category"]
        db_qg.author = qg["author"]
        db_qg.created = qg["created"]
        db_qg.kind = qg["kind"]
        db_qg.name = qg["name"]
        db_qg.description = qg["description"]

        db.commit()
        db.refresh(qg)
        return {'message': 'QG updated'}


@router.delete("/qgs/{id}")
def delete_qgs(id: int, db: Session = Depends(get_db)):
    qgs = db.query(QG).filter(QG.id == id).first()

    if qgs is None:
        return {"message": "QG not found"}
        # raise HTTPException(status_code=404, detail="Data not found")

    db.delete(qgs)
    db.commit()

    return {
        "result": "success",
        "deleted_id": id
    }