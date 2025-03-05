from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime
from pymongo import MongoClient
from bson.objectid import ObjectId
import pytz
import os

app = Flask(__name__)
app.secret_key = "nielit_secret_key_here"  # Required for flash messages

# MongoDB connection
MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://test:test@cluster0.sxci1.mongodb.net/?retryWrites=true&w=majority")
client = MongoClient(MONGO_URI)

# Database and Collection setup
db = client.todo_app  # Database name
todos = db.todos       # Collection name

# Home route to display all tasks
@app.route("/")
def index():
    ist = pytz.timezone("Asia/Kolkata")
    current_datetime = datetime.now(ist).strftime("%d-%m-%Y %I:%M %p")

    try:
        all_todos = list(todos.find().sort("created_at", -1))  # Sort by latest task
    except Exception as e:
        flash("Error fetching tasks!", "danger")
        all_todos = []  

    return render_template("index.html", todos=all_todos, datetime=current_datetime)

# Route to add a new task
@app.route("/add", methods=["POST"])
def add_todo():
    ist = pytz.timezone("Asia/Kolkata")
    current_datetime = datetime.now(ist).strftime("%d-%m-%Y %I:%M %p") 

    task = request.form.get("task")  # Get the task description
    if not task.strip():
        flash("Task cannot be empty!", "warning")
        return redirect(url_for("index"))

    try:
        todos.insert_one({"task": task, "created_at": current_datetime, "done": False})
        flash("Task added successfully!", "success")
    except Exception as e:
        flash("Error adding task!", "danger")

    return redirect(url_for("index"))

# Route to mark a task as complete
@app.route("/complete/<task_id>")
def complete_todo(task_id):
    try:
        todos.update_one({"_id": ObjectId(task_id)}, {"$set": {"done": True}})
        flash("Task marked as completed!", "info")
    except Exception as e:
        flash("Error updating task!", "danger")
    
    return redirect(url_for("index"))

# Route to delete a task
@app.route("/delete/<task_id>")
def delete_todo(task_id):
    try:
        todos.delete_one({"_id": ObjectId(task_id)})
        flash("Task deleted successfully!", "info")
    except Exception as e:
        flash("Error deleting task!", "danger")

    return redirect(url_for("index"))

# Route to update an existing task
@app.route("/update/<task_id>", methods=["GET", "POST"])
def update_todo(task_id):
    ist = pytz.timezone("Asia/Kolkata")
    current_datetime = datetime.now(ist).strftime("%d-%m-%Y %I:%M %p") 

    if request.method == "GET":
        try:
            task_to_update = todos.find_one({"_id": ObjectId(task_id)})
            return render_template("update.html", task=task_to_update)
        except Exception as e:
            flash("Error fetching task!", "danger")
            return redirect(url_for("index"))
    
    if request.method == "POST":
        updated_task = request.form.get("updated_task")
        if not updated_task.strip():
            flash("Task cannot be empty!", "warning")
            return redirect(url_for("update_todo", task_id=task_id))

        try:
            todos.update_one({"_id": ObjectId(task_id)}, {"$set": {"task": updated_task, "created_at": current_datetime}})
            flash("Task updated successfully!", "success")
        except Exception as e:
            flash("Error updating task!", "danger")

        return redirect(url_for("index"))

# Route to display task summary
@app.route("/summary")
def summary():
    try:
        total_tasks = todos.count_documents({})
        completed_tasks = todos.count_documents({"done": True})
        pending_tasks = todos.count_documents({"done": False})
    except Exception as e:
        flash("Error fetching summary!", "danger")
        total_tasks = completed_tasks = pending_tasks = 0

    return render_template(
        "summary.html",
        total_tasks=total_tasks,
        completed_tasks=completed_tasks,
        pending_tasks=pending_tasks
    )

if __name__ == "__main__":
    app.run(debug=True)  # Enable debug mode
