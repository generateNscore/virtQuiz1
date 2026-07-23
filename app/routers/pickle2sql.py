from fastapi import APIRouter, Depends #, HTTPException
import pickle
from sqlalchemy.orm import Session
from app.dependencies import get_db
from app.models import QG

# 이 파일은 오래전에 사용된 up8.pickle의 내용을 db에 저장하기 위해 만들었음.
#

router = APIRouter()


@router.post("/dump_pickle_2_sql")
def create_transaction(db: Session = Depends(get_db)):
    raw_data = pickle.load(open("QGset.pickle", "rb"))

    for k, v in raw_data.items():
        for k2, v2 in v.items():
            qg = QG(
                category = k,
                author = 'admin',
                created = '2020-01-01',
                kind = 'short',
                name = k2,
                description = v2['description'],
                questions = v2['Q'],
                answers = v2['A'],
                used = []
            )
            db.add(qg)
            db.commit()
            # print(k, k2)
