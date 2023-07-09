import pymongo
from app.Config import configs
from pymongo.errors import CollectionInvalid

client = pymongo.MongoClient(
    configs.MONGO_DB_URI)

DB = client[configs.MONGO_DBNAME]


def is_db_connected() -> bool:
    try:
        client.admin.command('ismaster')
        return True
    except:
        return False


def init_collection():
    try:
        DB.create_collection(
            "admin")
        DB.create_collection(
            "quiz")
        print(
            "✅ Collection Created.")
    except CollectionInvalid:
        print(
            "💫 Collection Already Exist.")


def get_admin_collection():
    ADMIN_COL = DB["admin"]
    return ADMIN_COL


def get_quiz_collection():
    QUIZ_COL = DB["quiz"]
    return QUIZ_COL
