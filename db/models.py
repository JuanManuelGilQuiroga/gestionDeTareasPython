from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

DATABASE_FILE = "taskManagerPython.db"
DATABASE_URL = f"sqlite:///{DATABASE_FILE}"

db_exists = os.path.exists(DATABASE_FILE)

engine = create_engine(DATABASE_URL, echo=True)
Session = sessionmaker(bind=engine)
Base = declarative_base()

class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    description = Column(String(255), nullable=True)
    completed = Column(Boolean, default=False)

if not db_exists:
    Base.metadata.create_all(engine)
    print(f"Base de datos creada en {DATABASE_FILE}")
else:
    print(f"Base de datos existente encontrada en {DATABASE_FILE}")
