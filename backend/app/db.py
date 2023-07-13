import pymongo
from app.Config import configs
from pymongo.errors import CollectionInvalid
from app.models.admin import Admin
from app.utils.hashing import hash_password
from datetime import datetime


client = pymongo.MongoClient(configs.MONGO_DB_URI)

DB = client[configs.MONGO_DBNAME]


def is_db_connected() -> bool:
    try:
        client.admin.command("ismaster")
        return True
    except:
        return False


def get_admin_collection():
    ADMIN_COL = DB["admin"]
    return ADMIN_COL


def get_quiz_collection():
    QUIZ_COL = DB["quiz"]
    return QUIZ_COL


def create_default_admin():
    ADMIN_COL = get_admin_collection()
    is_exist = ADMIN_COL.find_one({"email": configs.DEFAULT_ADMIN_EMAIL})
    if not is_exist:
        ADMIN_COL.insert_one(
            Admin(
                email=configs.DEFAULT_ADMIN_EMAIL,
                password=hash_password(str(configs.DEFAULT_ADMIN_PASSWORD)),
                name=configs.DEFAULT_ADMIN_NAME,
                created_at=datetime.now(),
            ).model_dump()
        )
        print("🔐 Created Default Admin.")
    else:
        print("🔐 Default Admin Already Exist.")


def init_collection():
    try:
        DB.create_collection("admin")
        DB.create_collection("quiz")
        print("✅ Collection Created.")
        DB["quiz"].create_index([("quiz_name", "text"), ("category", "text")])
        DB["admin"].create_index([("email", "text")])
    except CollectionInvalid:
        print("💫 Collection Already Exist.")
    finally:
        create_default_admin()
