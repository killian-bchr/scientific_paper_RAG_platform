from pydantic import BaseModel


class Domain(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True
