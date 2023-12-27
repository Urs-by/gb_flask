from fastapi import FastAPI
from models import Student
app = FastAPI()

students = []

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/students")
async def read_item():
    return students

@app.post('/student')
async def create_student(student: Student):
    students.append(student)
    return student