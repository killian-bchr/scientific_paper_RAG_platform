from pydantic import BaseModel


class Category(BaseModel):
    id: int
    name: str
    domain_id: int

    class Config:
        from_attributes = True
