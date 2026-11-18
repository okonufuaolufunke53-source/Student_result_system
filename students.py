"""Student records and student-management operations."""
from dataclasses import dataclass, asdict
from datetime import date
from typing import Dict, List, Optional


@dataclass
class Student:
    student_id: str
    full_name: str
    class_form: str
    gender: str
    date_of_birth: str
    scores: Dict[str, float]
    result_date: Optional[str] = None

    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict) -> "Student":
        return cls(
            student_id=str(data["student_id"]),
            full_name=str(data["full_name"]),
            class_form=str(data["class_form"]),
            gender=str(data["gender"]),
            date_of_birth=str(data["date_of_birth"]),
            scores={str(k): float(v) for k, v in data.get("scores", {}).items()},
            result_date=data.get("result_date"),
        )


def add_student(students: List[Student], student: Student) -> None:
    if find_student(students, student.student_id):
        raise ValueError("A student with that ID already exists.")
    students.append(student)


def find_student(students: List[Student], search_term: str) -> Optional[Student]:
    term = search_term.strip().lower()
    for student in students:
        if student.student_id.lower() == term or term in student.full_name.lower():
            return student
    return None


def update_student(student: Student, *, full_name=None, class_form=None,
                   gender=None, date_of_birth=None) -> None:
    if full_name is not None:
        student.full_name = full_name
    if class_form is not None:
        student.class_form = class_form
    if gender is not None:
        student.gender = gender
    if date_of_birth is not None:
        student.date_of_birth = date_of_birth


def delete_student(students: List[Student], student_id: str) -> bool:
    for index, student in enumerate(students):
        if student.student_id.lower() == student_id.strip().lower():
            del students[index]
            return True
    return False


def list_students(students: List[Student]) -> List[Student]:
    return sorted(students, key=lambda item: item.full_name.lower())
