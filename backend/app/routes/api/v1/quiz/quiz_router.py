from fastapi import APIRouter, status, Depends
from fastapi.requests import Request
from app.schemas.quiz import QuizOut, CreateQuiz
from app.oauth2 import get_current_admin
from app.services import service_create_quiz, service_delete_quiz, service_get_quizs, service_search_quiz, service_active_deactive_quiz

router = APIRouter()


@router.post("/", response_description="Add a new Quiz",
             status_code=status.HTTP_201_CREATED, response_model=QuizOut)
async def create_quiz(req: Request, create_quiz: CreateQuiz, current_admin=Depends(get_current_admin)):
    return service_create_quiz(create_quiz, current_admin)


@router.get("/search/", description="Search Quiz By Category or Quiz Name", status_code=status.HTTP_200_OK)
async def search_quiz(category:  str = None, quiz_name: str = None, limit: int = 10):
    return service_search_quiz(category, quiz_name, limit)


@router.get("/", description="Get Quiz", status_code=status.HTTP_200_OK)
async def get_quizs(req: Request, id: str = None, limit: int = 10):
    return service_get_quizs(id, limit)


@router.delete("/", description="Delete Quiz", status_code=status.HTTP_200_OK)
async def delete_quiz(req: Request, id: str, current_admin=Depends(get_current_admin)):
    return service_delete_quiz(id, current_admin)


@router.patch("/activate", description="Make Quiz Active", status_code=status.HTTP_200_OK)
async def delete_quiz(req: Request, id: str, current_admin=Depends(get_current_admin)):
    return service_active_deactive_quiz(id, current_admin, True)


@router.patch("/deactivate", description="Make Quiz Deactive", status_code=status.HTTP_200_OK)
async def delete_quiz(req: Request, id: str, current_admin=Depends(get_current_admin)):
    return service_active_deactive_quiz(id, current_admin, False)
