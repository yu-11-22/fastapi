from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
from crud import create_user, get_users
from validate import UserCreate

app = FastAPI()

# 初始化資料庫
Base.metadata.create_all(bind=engine)


# 資料庫 Session 共通程式碼部分
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users")
async def create_user_endpoint(user: UserCreate, db: Session = Depends(get_db)):
    new_user = create_user(db, name=user.name, email=user.email)
    return {"id": new_user.id, "name": new_user.name, "email": new_user.email}


@app.get("/users")
async def get_users_endpoint(db: Session = Depends(get_db)):
    return get_users(db)
