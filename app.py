import streamlit as st
from db.controllers import addTask, getTasks, markTaskCompleted, deleteCompletedTasks
from utils.file_io import exportTasks, importTasks

st.title("Gestión de Tareas")

# Agregar tareas
st.header("Agregar una nueva tarea")
title = st.text_input("Título de la tarea")
description = st.text_area("Descripción de la tarea")
if st.button("Agregar tarea"):
    if title:
        addTask(title, description)
        st.success("¡Tarea agregada con éxito!")
    else:
        st.error("El título de la tarea es obligatorio.")

# Listar tareas
tasks = getTasks()
st.header("Lista de tareas")
for task in tasks:
    col1, col2, col3 = st.columns([6, 2, 2])
    col1.write(f"**{task.title}** - {task.description}")
    col2.write("✔ Completada" if task.completed else "Pendiente")
    if not task.completed:
        if col3.button("Marcar como completada", key=f"complete-{task.id}"):
            markTaskCompleted(task.id)
            st.experimental_rerun()

# Eliminar tareas completadas
if st.button("Eliminar tareas completadas"):
    deleteCompletedTasks()
    st.success("¡Tareas completadas eliminadas con éxito!")
    st.experimental_rerun()

# Exportar e importar tareas
st.header("Exportar e importar tareas")
export_path = st.text_input("Ruta para exportar las tareas", "tasks.json")
if st.button("Exportar tareas"):
    exportTasks(export_path)
    st.success(f"¡Tareas exportadas a {export_path} con éxito!")

import_path = st.text_input("Ruta para importar las tareas", "tasks.json")
if st.button("Importar tareas"):
    try:
        importTasks(import_path)
        st.success(f"¡Tareas importadas desde {import_path} con éxito!")
        st.experimental_rerun()
    except Exception as e:
        st.error(f"Error al importar tareas: {e}")
