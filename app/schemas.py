from pydantic import BaseModel #, ConfigDict

# 1. 반환하고 싶은 컬럼만 정의한 Pydantic 모델 생성
class QgsCategoryOnly(BaseModel):
    id: int
    category: str
    count: int

    # class Config:
    #     # SQLAlchemy 모델 객체를 Pydantic이 읽을 수 있도록 설정
    #     from_attributes = True


class QgsNameOnly(BaseModel):
    id: int
    name: str

    # class Config:
    #     # SQLAlchemy 모델 객체를 Pydantic이 읽을 수 있도록 설정
    #     from_attributes = True