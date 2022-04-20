from todo import db


class TodoModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    desc = db.Column(db.String(100))
    category = db.Column(db.String(100))
    is_completed = db.Column(db.Boolean)


db.create_all()
