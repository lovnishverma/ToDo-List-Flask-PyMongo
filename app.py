from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB connection
client = MongoClient("your-mongodb-connection-string")
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
    todos.update_one({"_id": ObjectId(task_id)}, {"$set": {"done": True}})
    return redirect(url_for("index"))

@app.route("/delete/<task_id>")
def delete_todo(task_id):
    todos.delete_one({"_id": ObjectId(task_id)})
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run()
