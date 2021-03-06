from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:z7895123xb^@localhost/OJ'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

class Problem(db.Model):
    __tablename__ = 'problems'
    __table_args__ = {'mysql_charset': 'utf8'}
    problem_id = db.Column(db.Integer, primary_key=True)
    TimeLimit = db.Column(db.Integer, unique=False)
    MemoryLimit = db.Column(db.Integer, unique=False)
    ProblemHead = db.Column(db.String(200), unique=False)
    ProblemDescription = db.Column(db.Text, unique=False)
    Input = db.Column(db.Text, unique=False)
    Output = db.Column(db.Text, unique=False)
    SampleInput = db.Column(db.Text, unique=False)
    SampleOutput = db.Column(db.Text, unique=False)
    Hint = db.Column(db.Text, unique=False)
    Author = db.Column(db.String(200), unique=False)
    Source = db.Column(db.String(200), unique=False)


    def __init__(self,TimeLimit, MemoryLimit, ProblemHead, ProblemDescription, Input, Output, SampleInput, SampleOutput, Hint, Author, Source):
        self.problem_id = 1
        self.TimeLimit = int(TimeLimit)
        self.MemoryLimit = int(MemoryLimit)
        self.ProblemHead = ProblemHead
        self.ProblemDescription = ProblemDescription
        self.Input = Input
        self.Output = Output
        self.SampleInput = SampleInput
        self.SampleOutput = SampleOutput
        self.Hint = Hint
        self.Author = Author
        self.Source = Source


db.create_all()
problem_test = Problem(1000, 124000, 'test', 'test', 'test', 'test', 'test', 'test', 'test', 'admin', 'admin' )
db.session.add(problem_test)
db.session.commit()

