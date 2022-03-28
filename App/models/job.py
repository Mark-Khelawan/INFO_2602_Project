from App.database import db

class Job(db.model):
    jobId = db.Column(db.Integer, primary_key=True)
    jobPosition = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    industry = db.Column(db.String(100), nullable=False)
    subCategory = db.Column(db.String(100), nullable=False)
    competencies = db.Column(db.String(300), nullable=False)

    def competency_list(self):
        competenciey_string = self.competencies
        competencies = competenciey_string.split("; ")
        return competencies

    def toDict(self):
        return{
            'id': self.jobId,
            'position': self.jobPosition,
            'description': self.description,
            'industry': self.industry,
            'sub Category': self.subCategory,
            'competencies': self.competency_list()
        }