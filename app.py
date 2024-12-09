from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId  # Import ObjectId

app = Flask(__name__)

# MongoDB connection
client = MongoClient("mongodb+srv://test:test@cluster0.sxci1.mongodb.net/?retryWrites=true&w=majority")
db = client.todo_app  # Database name
todos = db.todos       # Collection name

@app.route("/")
def index():
    all_todos = todos.find()
    return render_template("index.html", todos=all_todos)

@app.route("/add", methods=["POST"])
def add_todo():
    task = request.form.get("task")
    if task:
        todos.insert_one({"task": task, "done": False})
    return redirect(url_for("index"))

@app.route("/complete/<task_id>")
def complete_todo(task_id):
    try:
        todos.update_one({"_id": ObjectId(task_id)}, {"$set": {"done": True}})
    except Exception as e:
        print(f"Error marking task as complete: {e}")
    return redirect(url_for("index"))

@app.route("/delete/<task_id>")
def delete_todo(task_id):
    try:
        todos.delete_one({"_id": ObjectId(task_id)})
    except Exception as e:
        print(f"Error deleting task: {e}")
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)  # Enable debug mode for better error visibility
