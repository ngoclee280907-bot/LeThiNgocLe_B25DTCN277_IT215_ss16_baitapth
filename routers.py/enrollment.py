from fastapi import APIRouter, HTTPException
from schemas import EnrollmentCreate
from data import (
    students,
    courses,
    enrollments
)
router = APIRouter(tags=["Enrollments"])

@router.post("/enrollments", status_code=201)
def create_enrollment(data: EnrollmentCreate):
    student = next((s for s in students if s["id"] == data.student_id), None)
    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )
    if student["status"] != "ACTIVE":
        raise HTTPException(
            status_code=400,
            detail="Student is not ACTIVE"
        )
    course = next((c for c in courses if c["id"] == data.course_id), None)
    if not course:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    if course["status"] != "OPEN":
        raise HTTPException(
            status_code=400,
            detail="Course is not OPEN"
        )
    enrollment_exists = next((e for e in enrollments
            if e["student_id"] == data.student_id
            and e["course_id"] == data.course_id
        ),
        None 
    )

    if enrollment_exists:
        raise HTTPException(
            status_code=400,
            detail="Enrollment already exists"
        )

    new_enrollment = {
        "id": len(enrollments) + 1,
        "student_id": data.student_id,
        "course_id": data.course_id
    }
    enrollments.append(new_enrollment)
    return {
        "message": "Enrollment created successfully",
        "data": new_enrollment
    }