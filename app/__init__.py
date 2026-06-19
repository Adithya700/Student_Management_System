from flask import Flask 
def create_app(): 
 
    app = Flask(__name__) 
 
    from app.routes.student_route import student_bp 
 
    app.register_blueprint(student_bp) 
 
    return app 