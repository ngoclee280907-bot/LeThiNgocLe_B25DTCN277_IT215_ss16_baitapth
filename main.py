from fastapi import FastAPI

from routers.student import router as student_router
from routers.enrollment import router as enrollment_router

app = FastAPI(
    title="Student Course Management API"
)

app.include_router(student_router)
app.include_router(enrollment_router)