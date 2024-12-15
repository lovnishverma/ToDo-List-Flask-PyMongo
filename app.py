from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId  # For handling MongoDB's ObjectId

app = Flask(__name__)


# MongoDB connection
# Connect to MongoDB Atlas using the provided connection string
# client = MongoClient("mongodb+srv://test:test@cluster0.sxci1.mongodb.net/?retryWrites=true&w=majority")
client = MongoClient("mongodb+srv://admin:123@cluster0.hh7q5.mongodb.net/?retryWrites=true&w=majority")
# Database and Collection setup
db = client.todo_app  # Database name
todos = db.todos       # Collection name

# Home route to display all tasks
@app.route("/")
def index():
    """
    Fetch all tasks from the MongoDB database and display them on the homepage.
    Each task includes:
    - Task description
    - Completion status (done or not done)
    """
    try:
        all_todos = todos.find()  # Retrieve all tasks from the "todos" collection
    except Exception as e:
        print("Error fetching tasks: {}".format(e))
        all_todos = []
    return render_template("index.html", todos=all_todos)

# Route to add a new task
@app.route("/add", methods=["POST"])
def add_todo():
    """
    Add a new task to the MongoDB database.
    - Accepts task description from the form.
    - Saves it with a default "not done" status.
    """
    task = request.form.get("task")  # Get the task description from the form
    if task:
        try:
            todos.insert_one({"task": task, "done": False})  # Insert the task into the collection
        except Exception as e:
            print("Error adding task: {}".format(e))
    return redirect(url_for("index"))

# Route to mark a task as complete
@app.route("/complete/<task_id>")
def complete_todo(task_id):
    """
    Mark a task as completed in the MongoDB database.
    - Finds the task by its ObjectId.
    - Updates the "done" field to True.
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
    Delete a task from the MongoDB database.
    - Finds the task by its ObjectId and removes it.
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
    Update a task in the MongoDB database.
    - GET request: Fetches the current task and displays it in an editable form.
    - POST request: Updates the task description in the database.
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
        # Update the task description in the database
        updated_task = request.form.get("updated_task")
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
    Display a summary of tasks using MongoDB aggregation.
    - Total tasks: Count of all documents in the collection.
    - Completed tasks: Count of documents where "done" is True.
    - Pending tasks: Count of documents where "done" is False.
    """
    try:
        total_tasks = todos.count_documents({})  # Count all tasks
        completed_tasks = todos.count_documents({"done": True})  # Count completed tasks
        pending_tasks = todos.count_documents({"done": False})  # Count pending tasks
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
