from settings import db
from sqlalchemy import func


class Mutants(db.Model):
    __tablename__ = "mutants"
    id = db.Column(db.Integer, primary_key=True)
    dna = db.Column(db.String(100))
    ismutant = db.Column(db.Boolean)

    def save_mutant(self):
        db.session.add(self)
        db.session.commit()

    def get_mutants_ratio(self):
        session = db.session
        result = session.query(Mutants.ismutant, func.count(Mutants.ismutant)).group_by(Mutants.ismutant).all()
        human = 0
        mutant = 0
        for value in result:
            if value[0] == True:
                mutant = value[1]
            else:
                human = value[1]
        return mutant, human, mutant/human