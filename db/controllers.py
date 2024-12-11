from .models import Session, Task

session = Session()

def addTask(title, description):
    task = Task(title=title, description=description)
    session.add(task)
    session.commit()

def getTasks():
    return session.query(Task).all()

def markTaskCompleted(taskId):
    task = session.query(Task).get(taskId)
    if task:
        task.completed = True
        session.commit()
        
def deleteCompletedTask(taskId):
    task = session.query(Task).get(taskId)
    if task.completed == True:
        session.delete(task)
        session.commit()
        
def deleteCompletedTasks():
    session.query(Task).filter(Task.completed == True).delete()
    session.commit()
    