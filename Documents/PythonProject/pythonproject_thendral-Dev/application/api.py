from flask.globals import request
from application.app import app

# Import your models here
from application.models import db, Question

@app.route("/")
def home():
    return {"Status": "Success"}, 200 

# Write your API endpoints here
@app.route("/question", methods=["POST"])
def question():

    """Craete Question
    {
        "title" = "This is title",
        "Description" = "Descrition123"
    } """

    params = request.json
    title = params.get("title")
    Description = params.get("Description")
 
    question = Question(title=title,Description=Description)

    # Make an actual entry in DB
    db.session.add(question)
    db.session.commit()
    return {
        "Status": "Success",
        "data": {
            "id": question.id,
            "title": question.title,
            "Description": question.Description,
        },
    }

@app.route("/questions", methods=["GET"])
def get_all_questions():
    questions = Question.query.filter().all()
    data = []
    for q in questions:
        data.append({
            #"id": question.id,
            "title": q.title,
            "Description": q.Description,
        })
        return {"Status": "Success","data":data},200

@app.route("/question/<int:id>", methods=["GET"])
def get_question_by_id(id):
    question = Question.query.filter_by(id=id).first()
    data = []
    #for q in questions:
    if question:
        data.append({
            "id": question.id,
            "title": question.title,
            "Description": question.Description,
        })
        return {"Status": "Success","data":data},200
    else:
        return {"Status": "Failure","Message":"Question not found"},404
