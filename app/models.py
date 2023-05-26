from app import db

model = db.Model
column = db.Column
string = db.String()
integer = db.Integer()
json = db.JSON()
boolean = db.Boolean()


class Quiz(model):
    __tablename__ = 'quiz'

    def __init__(self, question, op_1, op_2, op_3, op_4, answer):
        self.question = question
        self.op_1 = op_1
        self.op_2 = op_2
        self.op_3 = op_3
        self.op_4 = op_4
        self.answer = answer

    id = column(integer, primary_key=True)
    question = column(string)
    op_1 = column(string)
    op_2 = column(string)
    op_3 = column(string)
    op_4 = column(string)
    answer = column(string)

    def check_answer(self, answer):
        return self.answer == answer

