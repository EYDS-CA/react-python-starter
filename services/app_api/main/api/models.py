from main import db


class ExampleTable(db.Model):
    __tablename__ = 'example_table'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    string_field = db.Column(db.String(128), nullable=False)

    def __init__(self, string_field):
        self.string_field = string_field

    def to_json(self):
        return {
            'id': self.id,
            'name': self.string_field,
        }

# ADD MODELS AS NEEDED, SEISM PROJECT HAS A USER MODEL DEFINED THAT MAY BE USEFULL
