from flask import render_template, redirect, request, url_for, jsonify
from app import app, db
from .models import Quiz

def Index():
    return render_template('index.html')


def NewQuiz():
    if request.method == "POST":
        question = request.form['question']
        option_1  = request.form['option_1']
        option_2  = request.form['option_2']
        option_3  = request.form['option_3']
        option_4  = request.form['option_4']
        answer  = request.form['answer']
        add_quiz = Quiz(question=question, op_1=option_1, op_2=option_2, op_3=option_3, op_4=option_4, answer=answer)
        db.session.add(add_quiz)
        db.session.commit()
        return redirect(request.url)
    return render_template("add-quiz.html")


def GetQuiz(query=False):
    if query == False:
        get_quizes = Quiz.query.limit(5).all()
        temp = {}
        for x in get_quizes:
            temp[x.id] ={
                'question':x.question,
                'answer':x.answer,
                'options':[x.op_1, x.op_2, x.op_3, x.op_4]
            }
        return jsonify(temp)
    else:
        get_quiz = Quiz.query.filter_by(id=query).first()
        temp = {
            'id':get_quiz.id,
            'question':get_quiz.question,
            'answer':get_quiz.answer,
            'options':[get_quiz.op_1, get_quiz.op_2, get_quiz.op_3, get_quiz.op_4],
            'quiz_length':len(Quiz.query.all())
        }
        return jsonify(temp)


