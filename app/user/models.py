# création d'un models User

from datetime import datetime
from sqlalchemy import(
    Column,
    String,
    Integer,
    DateTime
)

from app.bd.database import Base

class User(Base):
    __tablename__='users'
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True, nullable=False)
    name = Column(String, nullable=False)
    hash_password = Column(String, nullable=False)
    created_date: datetime = Column(DateTime, default=datetime.now, index=True)
    