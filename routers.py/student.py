from fastapi import APIRouter, HTTPException

from data import (
    students,
    departments,
    enrollments,
    courses
)

router = APIRouter(tags=["Students"])

@router.get("/students/{student_id}")
def get_student_detail(student_id: int):

    student = next((s for s in students if s["id"] == student_id), None)
    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )
    department = next((d for d in departments if d["id"] == student["department_id"]), None)
    student_enrollments = [e for e in enrollments if e["student_id"] == student_id]
    student_courses = []
    for enrollment in student_enrollments:
        course = next((c for c in courses if c["id"] == enrollment["course_id"]), None)
        if course:
            student_courses.append(course)
    return {
        "student": student,
        "department": department,
        "courses": student_courses
    }