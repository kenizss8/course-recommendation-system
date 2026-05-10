from backend.database import get_database
from backend.sample_courses import SAMPLE_COURSES


def seed_courses():
    db = get_database()
    course_collection = db["courses"]
    inserted_or_updated = 0

    for course in SAMPLE_COURSES:
        result = course_collection.replace_one(
            {"title": course["title"]},
            course,
            upsert=True,
        )

        if result.upserted_id is not None or result.modified_count > 0:
            inserted_or_updated += 1

    total_courses = course_collection.count_documents({})

    print(f"Seed completed. Inserted/updated: {inserted_or_updated}")
    print(f"Total courses in database: {total_courses}")


if __name__ == "__main__":
    seed_courses()
