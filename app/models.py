from sqlalchemy import Column, Integer, String, Text
from database import Base

class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    plan = Column(String)
    genre = Column(String)
    service = Column(String)
    details = Column(Text)
