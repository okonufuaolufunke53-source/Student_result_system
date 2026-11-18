"""Score entry, validation, totals, averages and grading."""
from datetime import datetime
from typing import Dict
from students import Student

SUBJECTS = ("English", "Mathematics", "Biology", "Chemistry", "Physics")


def validate_score(score: float) -> float:
    score = float(score)
    if not 0 <= score <= 100:
        raise ValueError("Scores must be between 0 and 100.")
    return score


def record_scores(student: Student, scores: Dict[str, float]) -> None:
    if len(scores) < 5:
        raise ValueError("At least five subject scores are required.")
    student.scores = {subject: validate_score(score) for subject, score in scores.items()}
    student.result_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def calculate_total(student: Student) -> float:
    return sum(student.scores.values())


def calculate_average(student: Student) -> float:
    if not student.scores:
        return 0.0
    return calculate_total(student) / len(student.scores)


def calculate_grade(average: float) -> str:
    if average >= 70:
        return "A"
    if average >= 60:
        return "B"
    if average >= 50:
        return "C"
    if average >= 45:
        return "D"
    return "F"


def get_result(student: Student) -> dict:
    average = calculate_average(student)
    return {
        "total": calculate_total(student),
        "average": average,
        "grade": calculate_grade(average),
    }
