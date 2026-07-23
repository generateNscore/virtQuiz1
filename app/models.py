from sqlalchemy import Column, Integer, String, ARRAY, ForeignKey
# from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship
from app.database import Base
# from pgvector.sqlalchemy import Vector

class User(Base):
    __tablename__ = "urers"

    id = Column(Integer, primary_key=True, index=True)


class QG(Base):
    __tablename__ = "qgs"

    id = Column(Integer, primary_key=True, index=True)
    category = Column(String)
    author = Column(String)
    created = Column(String)
    kind = Column(String) # short/choice/action
    name = Column(String) # qg_name
    description = Column(String)
    questions = Column(ARRAY(String)) # list of strings
    answers = Column(String) # python code
    used = Column(ARRAY(String))

