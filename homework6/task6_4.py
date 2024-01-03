# Задание No4
# 📌 Напишите API для управления списком задач. Для этого создайте модель Task со следующими полями:
# ○ id: int (первичный ключ)
# ○ title: str (название задачи)
# ○ description: str (описание задачи)
# ○ done: bool (статус выполнения задачи)
# 📌 API должно поддерживать следующие операции:
# ○ Получение списка всех задач: GET /tasks/
# ○ Получение информации о конкретной задаче: GET /tasks/{task_id}/
# ○ Создание новой задачи: POST /tasks/
# ○ Обновление информации о задаче: PUT /tasks/{task_id}/
# ○ Удаление задачи: DELETE /tasks/{task_id}/
# 📌 Для валидации данных используйте параметры Field модели Task.
# 📌 Для работы с базой данных используйте SQLAlchemy и модуль databases.


from fastapi import FastAPI
from typing import List
from models import TaskIn, TaskOut
from database import tasks_db, engine, database

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get("/")
async def root():
    return {"message": "Hello hw6"}


@app.get("/tasks/", response_model=List[TaskOut])
async def read_users():
    query = tasks_db.select()
    return await database.fetch_all(query)


@app.post("/tasks/", response_model=TaskOut)
async def create_task(task: TaskIn):
    new_task = tasks_db.insert().values(**task.model_dump())
    new_id =await database.execute(new_task)
    return {**task.model_dump(), 'id': new_id}


@app.get("/tasks/{task_id}", response_model=TaskOut)
async def read_user(task_id: int):
    query = tasks_db.select().where(tasks_db.c.id == task_id)
    return await database.fetch_one(query)


@app.put("/tasks/{task_id}")
async def update_task(task_id: int, new_task: TaskIn):
    query = tasks_db.update().where(tasks_db.c.id ==
                                    task_id).values(**new_task.model_dump())
    await database.execute(query)
    return {'message': 'Task updated'}


@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    query = tasks_db.delete().where(tasks_db.c.id == task_id)
    await database.execute(query)
    return {'message': 'Task deleted'}