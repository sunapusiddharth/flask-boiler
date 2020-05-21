import uuid
import datetime

from app.main import db
from app.main.model.blogs import blogs
from ..util.decorator import token_required
from sqlalchemy import text
from sqlalchemy.orm import sessionmaker
from collections import namedtuple
from ... import engine

# Session = sessionmaker(bind=engine)
# session = Session()

@token_required
def save_new_blogs(data):
    blogs = blogs.query.filter_by(id=data['id']).first()
    if not blogs:
        new_blogs = blogs(
            id=str(uuid.uuid4()),
            name=data['name']
        )
        save_changes(new_blogs)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.'
        }
        return generate_token(new_blogs)
    else:
        response_object = {
            'status': 'fail',
            'message': 'blogs already exists. Please Log in.',
        }
        return response_object, 409

@token_required
def get_all_blogss():
    # return blogs.query.all()
    # replace the above with raw query to show raw query can also be used :
    sql = text('select * from blogs_test')
    result = db.session.execute(sql)
    for r in result:
        r_dict = dict(r.items())
        print("hi",r)
    return r_dict



def get_a_blogs(id):
    return blogs.query.filter_by(id=id).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()
