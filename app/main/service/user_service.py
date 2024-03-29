import uuid
import datetime

from app.main import db
from app.main.model.user import User
from ..util.decorator import token_required
from sqlalchemy import text
from sqlalchemy.orm import sessionmaker
from collections import namedtuple
from ... import engine

Session = sessionmaker(bind=engine)
session = Session()


def save_new_user(data):
    user = User.query.filter_by(email=data['email']).first()
    if not user:
        new_user = User(
            public_id=str(uuid.uuid4()),
            email=data['email'],
            username=data['username'],
            password=data['password'],
            registered_on=datetime.datetime.utcnow()
        )
        save_changes(new_user)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.'
        }
        return generate_token(new_user)
    else:
        response_object = {
            'status': 'fail',
            'message': 'User already exists. Please Log in.',
        }
        return response_object, 409

@token_required
def get_all_users():
    return User.query.all()
    # replace the above with raw query to show raw query can also be used :
    sql = text('select * from blogs_test')
    result = db.engine.execute(sql)
    Record = namedtuple('Record', result.keys())
    records = [Record(*r) for r in result.fetchall()]
    for r in records:
        print("hi",r)
    return records



def get_a_user(public_id):
    return User.query.filter_by(public_id=public_id).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()

def generate_token(user):
    try:
        # generate the auth token
        auth_token = user.encode_auth_token(user.id)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.',
            'Authorization': auth_token.decode()
        }
        return response_object, 201
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401