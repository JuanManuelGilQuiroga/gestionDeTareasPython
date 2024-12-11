import json
from db.models import Task, session

def exportTasks(filepath):
    tasks = session.query(Task).all()
    with open(filepath, 'w') as file:
        json.dump([
            {"id": task.id, "title": task.title, "description": task.description, "completed": task.completed}
            for task in tasks
        ], file)

def importTasks(filepath):
    with open(filepath, 'r') as file:
        tasks = json.load(file)
        for task_data in tasks:
            task = Task(
                id=task_data["id"],
                title=task_data["title"],
                description=task_data["description"],
                completed=task_data["completed"]
            )
            session.merge(task)
        session.commit()
