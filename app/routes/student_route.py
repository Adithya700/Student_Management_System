from flask import Blueprint, request, jsonify 
from app.services.student_service import (
    get_all_students,
    create_student,
    get_student_by_id,
    delete_student,
    update_student
)
student_bp = Blueprint( 
    "student", 
    __name__, 
    url_prefix="/students" 
) 
 
@student_bp.route("/", methods=["GET"]) 
def get_students(): 
    return jsonify(get_all_students())  
 
@student_bp.route("/", methods=["POST"]) 
def add_student(): 
    data = request.json
    if not data:
        return jsonify({"message": "Invalid data"}), 400
    create_student(data) 
    return jsonify({"message": "Student Created"}), 201

@student_bp.route("/<student_id>", methods=["GET"])
def get_student(student_id):
    student = get_student_by_id(student_id)

    if student:
        return jsonify(student)

    return jsonify({"message": "Student not found"}), 404

@student_bp.route("/<student_id>", methods=["DELETE"])
def remove_student(student_id):
    if delete_student(student_id):
        return jsonify({"message": "Student deleted"})

    return jsonify({"message": "Student not found"}), 404

@student_bp.route("/<student_id>", methods=["PUT"])
def edit_student(student_id):
    data = request.json

    student = update_student(student_id, data)

    if student:
        return jsonify(student)

    return jsonify({"message": "Student not found"}), 404