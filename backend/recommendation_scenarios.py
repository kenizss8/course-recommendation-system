from backend.recommendation_engine import generate_recommendations
from backend.sample_courses import SAMPLE_COURSES
from backend.schemas import RecommendRequest

SCENARIOS = [
    {
        "name": "Python beginner",
        "request": RecommendRequest(
            desired_category="Programming",
            desired_level="Beginner",
            keywords=["python", "logic"],
            description="Toi muon hoc Python co ban va ren luyen tu duy logic",
        ),
        "expected_top_course": "Python cho nguoi moi bat dau",
    },
    {
        "name": "Web beginner",
        "request": RecommendRequest(
            desired_category="Web Development",
            desired_level="Beginner",
            keywords=["react", "javascript"],
            description="Toi muon hoc lam giao dien web bang React va JavaScript",
        ),
        "expected_top_course": "ReactJS cho nguoi moi bat dau",
    },
    {
        "name": "Data beginner",
        "request": RecommendRequest(
            desired_category="Data Science",
            desired_level="Beginner",
            keywords=["python", "pandas", "data analysis"],
            description="Toi muon hoc phan tich du lieu bang Python va Pandas",
        ),
        "expected_top_course": "Data Analysis voi Python",
    },
]


def print_top_results(name, recommendations):
    print(f"\n=== {name} ===")
    for index, item in enumerate(recommendations[:3], start=1):
        print(
            f"{index}. {item['course']['title']} | total={item['total_score']} | "
            f"rule={item['rule_score']} | similarity={item['similarity_score']} | "
            f"matched={', '.join(item['matched_skills']) or 'none'}"
        )


def run_scenarios():
    failed_scenarios = []

    for scenario in SCENARIOS:
        recommendations = generate_recommendations(SAMPLE_COURSES, scenario["request"])
        print_top_results(scenario["name"], recommendations)

        top_course = recommendations[0]["course"]["title"] if recommendations else None
        if top_course != scenario["expected_top_course"]:
            failed_scenarios.append(
                (
                    scenario["name"],
                    scenario["expected_top_course"],
                    top_course,
                )
            )

    if failed_scenarios:
        print("\nScenario check failed:")
        for name, expected, actual in failed_scenarios:
            print(f"- {name}: expected '{expected}' but got '{actual}'")
        raise SystemExit(1)

    print("\nAll recommendation scenarios passed.")


if __name__ == "__main__":
    run_scenarios()
