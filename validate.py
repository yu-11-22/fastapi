from pydantic import BaseModel, EmailStr, constr


# 定義用來驗證的 Pydantic 模型，加入長度驗證
class UserCreate(BaseModel):
    name: constr(min_length=3, max_length=50)  # 使用者名稱，最少 3 字元，最多 50 字元
    email: EmailStr  # 電子郵件，會自動驗證 email 格式
