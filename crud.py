from sqlalchemy.orm import Session
from models import User


# 新增使用者
def create_user(db: Session, name: str, email: str):
    new_user = User(name=name, email=email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


# 查詢所有使用者
def get_users(db: Session):
    return db.query(User).all()
