from database.base import engine, Base
from database import tables

def init_db():
    Base.metadata.create_all(bind=engine)

def drop_db():
    Base.metadata.drop_all(bind=engine)

def reset_db():
    print("Dropping all tables...")
    drop_db()
    print("Recreating tables...")
    init_db()
    print("Database reset ✅")
