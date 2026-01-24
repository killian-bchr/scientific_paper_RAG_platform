from contextlib import contextmanager

from sqlalchemy.exc import SQLAlchemyError

from backend.database.base import SessionLocal


@contextmanager
def get_session(commit: bool = False):
    session = SessionLocal()
    try:
        yield session
        if commit:
            session.commit()

    except SQLAlchemyError:
        session.rollback()
        raise

    finally:
        session.close()
