from pydantic import BaseModel


class User(BaseModel):
    id: int
    username: str
    role: str

    class Config:
        from_attributes = True
