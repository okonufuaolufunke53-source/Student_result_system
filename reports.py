"""Text reports and class analysis."""
from pathlib import Path
from typing import List
from students import Student
from results import get_result


def student_report(student: Student) -> str:
    result = get_result(student)
    lines = [
        "=" * 48,
        "             STUDENT REPORT CARD",
        "=" * 48,
        f"Student ID : {student.student_id}",
        f"Full Name  : {student.full_name}",
        f"Class/Form : {student.class_form}",
        f"Gender     : {student.gender}",
        f"Date of Birth: {student.date_of_birth}",
        "-" * 48,
        "SUBJECT                         SCORE",
        "-" * 48,
    ]
    if student.scores:
        lines.extend(f"{subject:<30} {score:>7.1f}" for subject, score in student.scores.items())
    else:
        lines.append("No scores have been entered.")
    lines += [
        "-" * 48,
        f"Total   : {result['total']:.1f}",
        f"Average : {result['average']:.2f}",
        f"Grade   : {result['grade']}",
        f"Result entered: {student.result_date or 'Not yet entered'}",
        "=" * 48,
    ]
    return "\n".join(lines)


def class_report(students: List[Student], sort_by: str = "average") -> str:
    if sort_by == "name":
        ordered = sorted(students, key=lambda s: s.full_name.lower())
    else:
        ordered = sorted(students, key=lambda s: get_result(s)["average"], reverse=True)

    lines = ["STUDENT RESULT SUMMARY", "=" * 72,
             f"{'ID':<14}{'NAME':<25}{'TOTAL':>10}{'AVERAGE':>12}{'GRADE':>8}",
             "-" * 72]
    for student in ordered:
        result = get_result(student)
        lines.append(
            f"{student.student_id:<14}{student.full_name[:24]:<25}"
            f"{result['total']:>10.1f}{result['average']:>12.2f}{result['grade']:>8}"
        )

    averages = [get_result(s)["average"] for s in students if s.scores]
    lines += ["-" * 72]
    if averages:
        lines += [
            f"Highest average: {max(averages):.2f}",
            f"Lowest average : {min(averages):.2f}",
            f"Class average  : {sum(averages) / len(averages):.2f}",
        ]
    else:
        lines.append("Class statistics are unavailable because no scores have been entered.")
    return "\n".join(lines)


def save_report(content: str, filename: str = "class_report.txt") -> Path:
    report_dir = Path(__file__).resolve().parent / "reports"
    report_dir.mkdir(exist_ok=True)
    path = report_dir / filename
    path.write_text(content, encoding="utf-8")
    return path
