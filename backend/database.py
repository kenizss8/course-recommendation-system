import os
from pathlib import Path

from dotenv import load_dotenv
from pymongo import MongoClient

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

MONGODB_URL = os.getenv("MONGODB_URL", "mongodb://localhost:27017")
MONGODB_DB = os.getenv("MONGODB_DB", "course_recommender")

client = MongoClient(
    MONGODB_URL,
    serverSelectionTimeoutMS=5000,
    appname="course-recommendation-system",
)
db = client[MONGODB_DB]


def get_database():
    return db


def ping_database():
    client.admin.command("ping")
