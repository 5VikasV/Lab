
from flask import Flask, jsonify, request

app = Flask(__name__)

students = [
    {"id": 1, "name": "Rahul", "age": 20, "course": "Computer Science"},
    {"id": 2, "name": "Priya", "age": 21, "course": "Information Technology"}
]

# GET API - Retrieve all students
@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students)

# POST API - Add a new student
@app.route('/students', methods=['POST'])
def add_student():
    data = request.get_json()

    new_student = {
        "id": len(students) + 1,
        "name": data["name"],
        "age": data["age"],
        "course": data["course"]
    }

    students.append(new_student)
    return jsonify(new_student), 201

if __name__ == '__main__':
    app.run(debug=True)
