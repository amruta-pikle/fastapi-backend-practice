from typing import Dict, List

from fastapi import APIRouter, HTTPException, Depends, status
from app.Task_Manager_API.db import task_id_counter, tasks
from app.Task_Manager_API.model import Task
from app.Task_Manager_API.task_manager_auth import get_current_user

router = APIRouter(
    prefix='/taskmanager',
    tags=['Task Manager']
)

@router.post("/tasks", response_model=Dict)
def create_task(task : Task, current_user : dict = Depends(get_current_user)):
    if current_user["role"] != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only admins can create tasks"
        )
    global task_id_counter
    task_data = {"id": task_id_counter,"title": task.title,"description":task.description}
    tasks[task_id_counter]=task_data
    task_id_counter += 1
    return task_data

@router.get("/tasks", response_model=List[Dict])
def list_tasks():
    return list(tasks.values())

@router.put("/tasks/{task_id}", response_model=Dict)
def update_task(task_id: int, task: Task, current_user: dict = Depends(get_current_user)):
    if current_user["role"] != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="only admins can update the tasks"
        )

    if task_id not in tasks:
        raise HTTPException(status_code=404,detail="Task not found")

    tasks[task_id].update({"title":task.title,"description":task.description})
    return tasks[task_id]

@router.delete("/tasks/{task_id}",response_model=Dict)
def delete_task(task_id: int, current_user: dict = Depends(get_current_user)):
    if current_user["role"] != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="only admins can update the tasks"
        )

    if task_id not in tasks:
        raise HTTPException(
            status_code=404, detail="Task not found"
        )
    return tasks.pop(task_id)

