from . import db

class Locations(db.Model):
    """ """
    id = db.Column(db.Integer, primary_key = True)
    location = db.Column(db.String(100), nullable = False)
    country = db.Column(db.String(300), nullable = False)
    summary = db.Column(db.String(10000), nullable = True)
    wiki_link = db.Column(db.String(3000), nullable = True)
    image_link = db.Column(db.String(3000), nullable = True)

    def __repr__(self):
        return f"Locations: {self.location} - {self.country}"
