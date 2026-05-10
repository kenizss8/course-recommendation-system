from bson import ObjectId
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from backend.database import get_database, ping_database
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


def format_course(course):
    return {
        "id": str(course["_id"]),
        "title": course["title"],
        "category": course["category"],
        "level": course["level"],
        "description": course["description"],
        "skills": course.get("skills", []),
    }


def validate_object_id(course_id: str):
    if not ObjectId.is_valid(course_id):
        raise HTTPException(status_code=400, detail="Invalid course id")

    return ObjectId(course_id)


def normalize_text(value: str):
    return value.strip().lower()


def build_course_text(course):
    skills_text = " ".join(course.get("skills", []))
    return f"{course['title']} {course['description']} {skills_text}"


def calculate_rule_score(course, request_data: RecommendRequest):
    score = 0
    matched_skills = []

    if request_data.desired_category and normalize_text(course["category"]) == normalize_text(
        request_data.desired_category
    ):
        score += 2

    if request_data.desired_level and normalize_text(course["level"]) == normalize_text(
        request_data.desired_level
    ):
        score += 2

    course_skills = {normalize_text(skill) for skill in course.get("skills", [])}
    request_keywords = {normalize_text(keyword) for keyword in request_data.keywords if keyword.strip()}
    matched_skills = sorted(course_skills.intersection(request_keywords))
    score += len(matched_skills)

    return score, matched_skills


def calculate_similarity_scores(courses, request_data: RecommendRequest):
    request_text = f"{request_data.description} {' '.join(request_data.keywords)}".strip()

    if not request_text:
        return [0.0] * len(courses)

    course_texts = [build_course_text(course) for course in courses]
    documents = [request_text, *course_texts]

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(documents)
    similarity_values = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()

    return similarity_values.tolist()


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

    similarity_scores = calculate_similarity_scores(courses, request_data)
    recommendations = []

    for index, course in enumerate(courses):
        rule_score, matched_skills = calculate_rule_score(course, request_data)
        similarity_score = round(similarity_scores[index], 4)
        total_score = round(rule_score + (similarity_score * 3), 4)

        recommendations.append(
            {
                "course": format_course(course),
                "rule_score": rule_score,
                "similarity_score": similarity_score,
                "total_score": total_score,
                "matched_skills": matched_skills,
            }
        )

    recommendations.sort(key=lambda item: item["total_score"], reverse=True)

    return {
        "message": "Recommendations generated successfully",
        "recommendations": recommendations[:5],
    }
