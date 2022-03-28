from App.database import db

class Job_Listing(db.model):
    listingId = db.Column(db.Integer, nullable=False)
    