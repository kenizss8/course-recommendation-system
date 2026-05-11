from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

CATEGORY_MATCH_SCORE = 3
LEVEL_MATCH_SCORE = 1
KEYWORD_MATCH_SCORE = 1
SIMILARITY_WEIGHT = 3
DEFAULT_RECOMMENDATION_LIMIT = 3


def format_course(course):
    return {
        "id": str(course["_id"]) if "_id" in course else "",
        "title": course["title"],
        "category": course["category"],
        "level": course["level"],
        "description": course["description"],
        "skills": course.get("skills", []),
    }


def normalize_text(value: str):
    return value.strip().lower()


def build_course_text(course):
    skills_text = " ".join(course.get("skills", []))
    return f"{course['title']} {course['description']} {skills_text}"


def calculate_rule_score(course, request_data):
    score = 0

    if request_data.desired_category and normalize_text(course["category"]) == normalize_text(
        request_data.desired_category
    ):
        score += CATEGORY_MATCH_SCORE

    if request_data.desired_level and normalize_text(course["level"]) == normalize_text(
        request_data.desired_level
    ):
        score += LEVEL_MATCH_SCORE

    course_skills = {normalize_text(skill) for skill in course.get("skills", [])}
    request_keywords = {normalize_text(keyword) for keyword in request_data.keywords if keyword.strip()}
    matched_skills = sorted(course_skills.intersection(request_keywords))
    score += len(matched_skills) * KEYWORD_MATCH_SCORE

    return score, matched_skills


def calculate_similarity_scores(courses, request_data):
    request_text = f"{request_data.description} {' '.join(request_data.keywords)}".strip()

    if not request_text:
        return [0.0] * len(courses)

    course_texts = [build_course_text(course) for course in courses]
    documents = [request_text, *course_texts]

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(documents)
    similarity_values = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()

    return similarity_values.tolist()


def generate_recommendations(courses, request_data, limit: int = DEFAULT_RECOMMENDATION_LIMIT):
    similarity_scores = calculate_similarity_scores(courses, request_data)
    recommendations = []

    for index, course in enumerate(courses):
        rule_score, matched_skills = calculate_rule_score(course, request_data)
        similarity_score = round(similarity_scores[index], 4)
        total_score = round(rule_score + (similarity_score * SIMILARITY_WEIGHT), 4)

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
    return recommendations[:limit]
