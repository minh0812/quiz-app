from pydantic import BaseModel


class Collections(BaseModel):
    title: str

class Questions(BaseModel):
    id: int
    title: str
    answers1: str
    answers2: str
    answers3: str
    answers4: str
    correct_answer: str