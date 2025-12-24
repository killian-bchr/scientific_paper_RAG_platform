from contextlib import contextmanager
from database.base import SessionLocal


@contextmanager
def get_session():
    session = SessionLocal()
    try:
        yield session

    except:
        session.rollback()
        raise

    finally:
        session.close()
