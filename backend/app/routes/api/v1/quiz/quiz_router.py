from fastapi import APIRouter, status
from fastapi.requests import Request
from app.models.quiz import Quiz
from app.schemas.quiz import QuizOut, CreateQuiz
from app.db import get_quiz_collection
from app.utils.serializer import serializeDict, serializeList
from fastapi.exceptions import HTTPException
from datetime import datetime
from bson import ObjectId
from typing import List


router = APIRouter()

QUIZ_COL = get_quiz_collection()


@router.post("/", response_description="Add a new Quiz",
             status_code=status.HTTP_201_CREATED, response_model=QuizOut)
async def create_quiz(req: Request, create_quiz: CreateQuiz):

    if len(create_quiz.questions) == 0:
        raise HTTPException(status_code=status.HTTP_304_NOT_MODIFIED,
                            detail="Please follow correct format to add Quiz.")
    total_marks = 0
    for ques in create_quiz.questions:
        total_marks += ques.marks

    quiz = Quiz(added_by_id="64aaf6a3ed60db9d757b0467", added_by_name="Neeraj Kumar", total_marks=total_marks, created_at=datetime.now(),
                **create_quiz.model_dump())
    _id = QUIZ_COL.insert_one(
        quiz.model_dump())
    return_quiz = QUIZ_COL.find_one(
        _id.inserted_id)
    return serializeDict(return_quiz)


@router.get("/{id}", description="Get Quiz", status_code=status.HTTP_200_OK, response_model=QuizOut)
async def search_quiz_by_id(req: Request, id: str):
    quiz_exist = QUIZ_COL.find_one(
        {"_id": ObjectId(id)})
    if quiz_exist:
        return serializeDict(quiz_exist)
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Quiz not found")


@router.get("/", description="Get all Quiz", status_code=status.HTTP_200_OK)
async def get_all_quiz(limit: int = 10):
    quiz_exist = QUIZ_COL.find(
        {}).limit(limit)
    if quiz_exist:
        return serializeList(
            quiz_exist)
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Quiz not found")
