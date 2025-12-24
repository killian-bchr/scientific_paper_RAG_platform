from contextlib import contextmanager

from sqlalchemy.exc import SQLAlchemyError

from database.base import SessionLocal


@contextmanager
def get_session():
    session = SessionLocal()
    try:
        yield session

    except SQLAlchemyError:
        session.rollback()
        raise

    finally:
        session.close()
