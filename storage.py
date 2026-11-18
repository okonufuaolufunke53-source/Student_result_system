"""JSON persistence for student records."""
import json
from pathlib import Path
from typing import List
from students import Student

DATA_DIR = Path(__file__).resolve().parent / "data"
DATA_FILE = DATA_DIR / "students.json"


def load_students() -> List[Student]:
    if not DATA_FILE.exists():
        return []
    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            records = json.load(file)
        return [Student.from_dict(item) for item in records]
    except (json.JSONDecodeError, KeyError, TypeError, ValueError) as error:
        raise RuntimeError(f"Could not read student data: {error}") from error


def save_students(students: List[Student]) -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    temporary_file = DATA_FILE.with_suffix(".tmp")
    with temporary_file.open("w", encoding="utf-8") as file:
        json.dump([student.to_dict() for student in students], file, indent=4)
    temporary_file.replace(DATA_FILE)
