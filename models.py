from app import db


class Country(db.Model):
    __tablename__ = 'countries'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60))

    def __repr__(self):
        return '<Country: {}>'.format(self.name)


class State(db.Model):
    __tablename__ = 'state'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60))
    country_id = db.Column(db.Integer)

    def __repr__(self):
        return '<State: {}>'.format(self.name)  


class City(db.Model):
    __tablename__ = 'city'
    id = db.Column(db.Integer, primary_key=True)
    state = db.Column(db.String(60))
    name = db.Column(db.String(60))
    stateid = db.Column(db.Integer) 

    def __repr__(self):
        return '<City: {}>'.format(self.name)