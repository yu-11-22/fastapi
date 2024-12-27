from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 設置資料庫連線的 url
DATABASE_URL = "mysql+pymysql://root:root@127.0.0.1:3306/testdb"

# 基於連線 url 建立資料庫引擎
engine = create_engine(DATABASE_URL)

"""
使用 sessionmaker 可以用來創建 session 類別
autocommit=False：不自動提交，需手動執行 commit 操作
autoflush=False：避免在查詢時自動刷寫資料庫，可以在需要時手動刷新資料
bind=engine：綁定會話到設定好的資料庫引擎
"""
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 定義 Base 使用 ORM 方式互動，讓所有模型都可以繼承此基類
Base = declarative_base()