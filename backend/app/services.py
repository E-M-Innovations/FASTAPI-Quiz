from app.db import get_quiz_collection, get_admin_collection
from fastapi.exceptions import HTTPException
from fastapi import status
from app.utils.serializer import serializeDict, serializeList
from bson import ObjectId
from bson.errors import InvalidId
from app.models.quiz import Quiz
from app.models.admin import Admin
from datetime import datetime
from app.utils.hashing import hash_password

QUIZ_COL = get_quiz_collection()
ADMIN_COL = get_admin_collection()


#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#
#           QUIZ SERVICES
#
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

def service_create_quiz(create_quiz, current_admin):
    if len(create_quiz.questions) == 0:
        raise HTTPException(status_code=status.HTTP_206_PARTIAL_CONTENT,
                            detail="Please follow correct format to add Quiz.")
    total_marks = 0
    for ques in create_quiz.questions:
        total_marks += ques.marks
        single_true_option = 0

        #! Making sure there exist an option which is correct
        for opt in ques.options:
            if opt.is_correct:
                single_true_option += 1
        if single_true_option != 1:
            raise HTTPException(status_code=status.HTTP_206_PARTIAL_CONTENT,
                                detail="Please make sure question '{}' have only one correct option.".format(ques.question))

    current_admin = serializeDict(
        current_admin)
    quiz = Quiz(added_by_id=current_admin["_id"], added_by_name=current_admin["name"], total_marks=total_marks, created_at=datetime.now(),
                **create_quiz.model_dump())
    _id = QUIZ_COL.insert_one(
        quiz.model_dump())
    return_quiz = QUIZ_COL.find_one(
        _id.inserted_id)
    return serializeDict(return_quiz)


def service_search_quiz(category, quiz_name, limit):
    if category and quiz_name:
        return get_results(category + " " + quiz_name, limit)
    if category:
        return get_results(category, limit)
    elif quiz_name:
        return get_results(quiz_name, limit)

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Request")


def service_get_quizs(id, limit):
    if id is not None:
        try:
            quiz_exist = QUIZ_COL.find_one(
                {"_id": ObjectId(id)})
        except InvalidId:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="invalid id")
        if quiz_exist:
            return serializeDict(quiz_exist)
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Quiz not found")

    #! It will return all quizzes with limit
    quiz_exist = QUIZ_COL.find(
        {}).sort("created_at", -1).limit(limit)  # Sorted By Created AT Recent quiz will come first
    if quiz_exist:
        return serializeList(
            quiz_exist)
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Quiz not found")


def service_delete_quiz(id, current_admin):
    current_admin = serializeDict(
        current_admin)
    try:
        filter = {"_id": ObjectId(id)}
    except InvalidId:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="invalid id")

    found_row = QUIZ_COL.find_one(
        filter)
    if not found_row:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Quiz not found")

    QUIZ_COL.delete_one(filter)
    return {"detail": "Quiz deleted"}


def service_active_deactive_quiz(id: str, current_admin, is_active=True):
    current_admin = serializeDict(
        current_admin)
    try:
        filter = {"_id": ObjectId(id)}
    except InvalidId:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="invalid id")

    found_row = QUIZ_COL.find_one(
        filter)
    if not found_row:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Quiz not found")
    if is_active:
        new_vals = {
            "$set": {"is_active": True}}
        QUIZ_COL.update_one(
            filter, new_vals)
        return {"detail": "Quiz is active now."}
    new_vals = {
        "$set": {"is_active": False}}
    QUIZ_COL.update_one(
        filter, new_vals)
    return {"detail": "Quiz is deactivated."}


def get_results(search_by: str, limit: int):
    search_result = QUIZ_COL.find(
        {"$text":
            {
                "$search": search_by,
                "$caseSensitive": False

            }
         }
    ).sort("created_at", -1).limit(limit)
    res = serializeList(
        search_result)
    if len(res) == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Quiz not found")
    return res


#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#
#           ADMIN SERVICES
#
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


def service_admin_create_account(admin):
    admin_exist = ADMIN_COL.find_one(
        {"email": admin.email})
    if admin_exist:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail=f"User with email {admin.email} already exist.")
    admin.password = hash_password(
        admin.password)
    admin = Admin(
        created_at=datetime.now(), **admin.model_dump())
    _id = ADMIN_COL.insert_one(
        admin.model_dump())

    return_admin = ADMIN_COL.find_one(
        _id.inserted_id)

    return serializeDict(return_admin)
