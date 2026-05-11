from bson import ObjectId
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from backend.database import get_database, ping_database
from backend.recommendation_engine import format_course, generate_recommendations
from backend.schemas import CourseCreate, CourseUpdate, RecommendRequest

app = FastAPI(title="Course Recommendation API")

# Cho phep frontend React (Vite) goi API tu localhost:5173
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

db = get_database()
course_collection = db["courses"]


def validate_object_id(course_id: str):
    if not ObjectId.is_valid(course_id):
        raise HTTPException(status_code=400, detail="Invalid course id")

    return ObjectId(course_id)


@app.get("/")
def read_root():
    return {"message": "FastAPI backend is running"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/db-health")
def database_health_check():
    try:
        ping_database()
        return {
            "status": "ok",
            "database": "connected",
            "message": "MongoDB connection successful",
        }
    except Exception as error:
        return {
            "status": "error",
            "database": "disconnected",
            "message": str(error),
        }


@app.get("/courses")
def get_courses():
    courses = course_collection.find()
    return [format_course(course) for course in courses]


@app.post("/courses")
def create_course(course: CourseCreate):
    new_course = course.model_dump()
    result = course_collection.insert_one(new_course)
    created_course = course_collection.find_one({"_id": result.inserted_id})

    return {
        "message": "Course created successfully",
        "course": format_course(created_course),
    }


@app.put("/courses/{course_id}")
def update_course(course_id: str, course: CourseUpdate):
    object_id = validate_object_id(course_id)
    existing_course = course_collection.find_one({"_id": object_id})

    if not existing_course:
        raise HTTPException(status_code=404, detail="Course not found")

    updated_data = course.model_dump()
    course_collection.update_one({"_id": object_id}, {"$set": updated_data})
    updated_course = course_collection.find_one({"_id": object_id})

    return {
        "message": "Course updated successfully",
        "course": format_course(updated_course),
    }


@app.delete("/courses/{course_id}")
def delete_course(course_id: str):
    object_id = validate_object_id(course_id)
    existing_course = course_collection.find_one({"_id": object_id})

    if not existing_course:
        raise HTTPException(status_code=404, detail="Course not found")

    course_collection.delete_one({"_id": object_id})

    return {"message": "Course deleted successfully"}


@app.post("/recommend")
def recommend_courses(request_data: RecommendRequest):
    courses = list(course_collection.find())

    if not courses:
        return {
            "message": "No courses found in database",
            "recommendations": [],
        }

    recommendations = generate_recommendations(courses, request_data)

    return {
        "message": "Recommendations generated successfully",
        "recommendations": recommendations,
    }
