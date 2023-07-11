from pydantic import BaseModel, field_validator
from typing import List
from datetime import datetime


class Options(BaseModel):
    option: str
    is_correct: bool


class Question(BaseModel):
    question: str
    options: List[Options]
    marks: int

    @field_validator("question", mode="before")
    def validate_question(cls, v: str):
        return v.capitalize()


class Quiz(BaseModel):
    """
    It conatins database model for the quiz questions.
    """

    quiz_name: str
    category: str
    questions: List[Question]
    total_marks: int
    added_by_name: str
    added_by_id: str
    is_active: bool = False
    total_completed: int = 0
    created_at: datetime
