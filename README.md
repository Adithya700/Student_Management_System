
# Student Management API

A RESTful API built using **Flask** and **Blueprints** for managing student records. The API supports CRUD (Create, Read, Update, Delete) operations and stores student information in a SQLite database.

---

## Features

* Retrieve all students
* Retrieve a student by ID
* Add a new student
* Update student details
* Delete a student
* Modular architecture using Flask Blueprints
* Persistent storage with SQLite
* JSON-based REST API

---

##  Tech Stack

* Python
* Flask 
* SQLite 
* Flask Blueprints
* JSON

---

##  Project Structure

```text
student-management-api/
│
├── app/
│   ├── routes/
│   │   └── student_routes.py
│   ├── services/
│   │   └── student_service.py
│   ├── models/
│        └── student.py
│   
│
├
├── run.py
├── requirements.txt
└── README.md
```

---


##  API Endpoints

### Get All Students

**Endpoint**

```http
GET /students/
```

**Response**

```json
[
  {
    "id": "S101",
    "name": "Alice",
    "age": 20,
    "course": "Computer Science"
  }
]
```

---

### Get Student by ID

**Endpoint**

```http
GET /students/<student_id>
```

**Response**

```json
{
  "id": "S101",
  "name": "Alice",
  "age": 20,
  "course": "Computer Science"
}
```

If the student does not exist:

```json
{
  "message": "Student not found"
}
```

Status Code: `404 Not Found`

---

### Add Student

**Endpoint**

```http
POST /students/
```

**Request Body**

```json
{
  "id": "S101",
  "name": "Alice",
  "age": 20,
  "course": "Computer Science"
}
```

**Response**

```json
{
  "message": "Student Created"
}
```

Status Code: `201 Created`

---

### Update Student

**Endpoint**

```http
PUT /students/<student_id>
```

**Request Body**

```json
{
  "name": "Alice Johnson",
  "age": 21,
  "course": "Data Science"
}
```

**Response**

```json
{
  "id": "S101",
  "name": "Alice Johnson",
  "age": 21,
  "course": "Data Science"
}
```

If the student does not exist:

```json
{
  "message": "Student not found"
}
```

Status Code: `404 Not Found`

---

### Delete Student

**Endpoint**

```http
DELETE /students/<student_id>
```

**Response**

```json
{
  "message": "Student deleted"
}
```

If the student does not exist:

```json
{
  "message": "Student not found"
}
```

Status Code: `404 Not Found`

---

##  Installation and Setup

### Clone the Repository

```bash
git clone https://github.com/your-username/student-management-api.git
cd student-management-api
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
python run.py
```

The server will start at:

```text
http://127.0.0.1:5000/
```

---

##  Testing the API

You can test the endpoints using:

* Postman
* Thunder Client
* curl

Example:

```bash
curl http://127.0.0.1:5000/students/
```


##  Author

Adithya k.s

Built using Flask to practice REST API development, and layered application architecture.
