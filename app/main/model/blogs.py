from .. import db
import datetime

class blogs(db.Model):
    """ blogs Model for storing blogs related details """
    __tablename__ = "blogs"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100))

    def __repr__(self):
        return "<blogs '{}'>".format(self.blogsname)

   