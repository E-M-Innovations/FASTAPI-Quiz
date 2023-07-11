from pydantic import BaseModel, Field, ConfigDict, field_validator
from typing import List
from app.models.quiz import Question, Quiz


class CreateQuiz(BaseModel):
    quiz_name: str
    category: str
    questions: List[Question]

    @field_validator("quiz_name", mode="before")
    def validate_quiz_name(cls, v: str):
        return v.upper()

    @field_validator("category", mode="before")
    def validate_category(cls, v: str):
        return v.upper()

    model_config = ConfigDict(
        str_strip_whitespace=True,
        from_attributes=True,
        populate_by_name=True,
        json_schema_extra={
            "example": {
                "quiz_name": "string",
                "category": "string",
                "questions": [
                    {
                        "question": "string",
                        "options": [
                            {"option": "string", "is_correct": True},
                            {"option": "string", "is_correct": False},
                        ],
                        "marks": 0,
                    }
                ],
            }
        },
    )


class QuizOut(Quiz):
    id: str = Field(alias="_id")

    model_config = ConfigDict(
        str_strip_whitespace=True,
        from_attributes=True,
        populate_by_name=True,
        json_schema_extra={
            "example": {
                "_id": "string",
                "quiz_name": "string",
                "category": "string",
                "questions": [
                    {
                        "question": "string",
                        "options": [
                            {"option": "string", "is_correct": False},
                            {"option": "string", "is_correct": False},
                            {"option": "string", "is_correct": True},
                        ],
                        "marks": 0,
                    },
                ],
                "total_marks": 0,
                "added_by_name": "string",
                "added_by_id": "string",
                "is_active": False,
                "created_at": "string",
            }
        },
    )


#! need to solve PyobjectID
# class Quizs(BaseModel):
#     quizs: List[QuizOut]

#     model_config = ConfigDict(
#         str_strip_whitespace=True, from_attributes=True, populate_by_name=True, json_schema_extra={
#             "example": {
#                 "quizs": [{
#                     "_id": "string",
#                     "quiz_name": "string",
#                     "category": "string",
#                     "questions": [
#                         {
#                             "question": "string",
#                             "options": [
#                                 {
#                                     "option": "string",
#                                     "is_correct": False
#                                 },
#                                 {
#                                     "option": "string",
#                                     "is_correct": True
#                                 },
#                                 {
#                                     "option": "string",
#                                     "is_correct": False
#                                 }
#                             ],
#                             "marks": 0
#                         },
#                     ],
#                     "total_marks": 0,
#                     "added_by_name": "string",
#                     "added_by_id": "string",
#                     "is_active": False,
#                     "created_at": "string",

#                 }

#                 ]}})
