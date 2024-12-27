from sqlalchemy import Column, Integer, String
from database import Base

# 基於 base 的一張 user 資料表
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
