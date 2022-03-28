from App.database import db

class Course(db.model):
    courseCode = db.Column(db.Integer, primary_key=True)
    courseName = db.Column(db.String(100), nullable=False)
    competencyOutcome = db.Column(db.String(300), nullable=False)

    def toDict(self):
        return {
            'course code': self.courseCode,
            'coure name': self.courseName,
            'competency outcome': self.competencyOutcome
        }