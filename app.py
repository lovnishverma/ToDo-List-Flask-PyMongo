from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId  # For handling MongoDB's ObjectId

app = Flask(__name__)

# MongoDB connection
client = MongoClient("mongodb+srv://test:test@cluster0.sxci1.mongodb.net/?retryWrites=true&w=majority")
db = client.todo_app  # Database name
todos = db.todos       # Collection name

# Home route to display all tasks
@app.route("/")
def index():
    """
    Fetch all tasks from the database and display them on the homepage.
    """
    try:
        all_todos = todos.find()  # Fetch all tasks
    except Exception as e:
        print("Error fetching tasks: {}".format(e))
        all_todos = []
    return render_template("index.html", todos=all_todos)

# Route to add a new task
@app.route("/add", methods=["POST"])
def add_todo():
    """
    Add a new task to the database.
    """
    task = request.form.get("task")  # Get the task from the form
    if task:
        try:
            todos.insert_one({"task": task, "done": False})  # Add task to the database
        except Exception as e:
            print("Error adding task: {}".format(e))
    return redirect(url_for("index"))

# Route to mark a task as complete
@app.route("/complete/<task_id>")
def complete_todo(task_id):
    """
    Mark a task as completed based on its ID.
    """
    try:
        todos.update_one({"_id": ObjectId(task_id)}, {"$set": {"done": True}})
    except Exception as e:
        print("Error marking task as complete: {}".format(e))
    return redirect(url_for("index"))

# Route to delete a task
@app.route("/delete/<task_id>")
def delete_todo(task_id):
    """
    Delete a task from the database based on its ID.
    """
    try:
        todos.delete_one({"_id": ObjectId(task_id)})
    except Exception as e:
        print("Error deleting task: {}".format(e))
    return redirect(url_for("index"))

# Route to update an existing task
@app.route("/update/<task_id>", methods=["GET", "POST"])
def update_todo(task_id):
    """
    Display the current task in an editable form and update it.
    """
    if request.method == "GET":
        # Fetch the task to be updated
        try:
            task_to_update = todos.find_one({"_id": ObjectId(task_id)})
            return render_template("update.html", task=task_to_update)
        except Exception as e:
            print("Error fetching task for update: {}".format(e))
            return redirect(url_for("index"))
    
    if request.method == "POST":
        # Update the task in the database
        updated_task = request.form.get("updated_task")  # Get updated task description
        if updated_task:
            try:
                todos.update_one({"_id": ObjectId(task_id)}, {"$set": {"task": updated_task}})
            except Exception as e:
                print("Error updating task: {}".format(e))
        return redirect(url_for("index"))

# Route to display task summary using aggregation
@app.route("/summary")
def summary():
    """
    Display a summary of tasks (total, completed, pending).
    """
    try:
        total_tasks = todos.count_documents({})  # Total tasks
        completed_tasks = todos.count_documents({"done": True})  # Completed tasks
        pending_tasks = todos.count_documents({"done": False})  # Pending tasks
    except Exception as e:
        print("Error fetching summary: {}".format(e))
        total_tasks = completed_tasks = pending_tasks = 0

    return render_template(
        "summary.html",
        total_tasks=total_tasks,
        completed_tasks=completed_tasks,
        pending_tasks=pending_tasks
    )

if __name__ == "__main__":
    app.run(debug=True)  # Enable debug mode for better error visibility
