from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory task list
tasks = []

# Home route
@app.route('/')
def home():
    return (
        "Welcome to the Flask Task Manager!\n"
        "Available endpoints:\n"
        "- GET /tasks: List all tasks\n"
        "- POST /add: Add a new task (provide 'task' in JSON body)\n"
        "- POST /done/<task_id>: Mark a task as done\n"
        "- GET /api/tasks: Get tasks as JSON\n"
    )

# List all tasks
@app.route('/tasks', methods=['GET'])
def list_tasks():
    if not tasks:
        return "No tasks available."
    response = "Tasks:\n"
    for task in tasks:
        status = "✔ Done" if task["done"] else "❌ Not Done"
        response += f"- {task['id']}: {task['task']} [{status}]\n"
    return response

# Add a new task
@app.route('/add', methods=['POST'])
def add_task():
    data = request.get_json()
    if not data or "task" not in data:
        return "Error: Provide a 'task' in JSON body.", 400
    new_task = {"id": len(tasks) + 1, "task": data["task"], "done": False}
    tasks.append(new_task)
    return f"Task '{data['task']}' added successfully!"



# Mark a task as done
@app.route('/done/<int:task_id>', methods=['POST'])
def mark_done(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            return f"Task {task_id} marked as done."
    return f"Task {task_id} not found.", 404



# API to get tasks as JSON
@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)



if __name__ == '__main__':
    app.run(debug=True)
