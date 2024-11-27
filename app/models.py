from . import db

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    math_score = db.Column(db.Integer, nullable=False)
    science_score = db.Column(db.Integer, nullable=False)
    english_score = db.Column(db.Integer, nullable=False)

    def calculate_average(self):
        return (self.math_score + self.science_score + self.english_score) / 3

    def is_passing(self, passing_score=40):
        return all(score >= passing_score for score in [self.math_score, self.science_score, self.english_score])
