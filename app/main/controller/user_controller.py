from flask import request
from flask_restx import Resource

from ..util.dto import UserDto
from ..service.user_service import save_new_user, get_all_users, get_a_user

api = UserDto.api
_user = UserDto.user


@api.route('/')
class UserList(Resource):
    @api.doc('list_of_registered_users')
    @api.marshal_list_with(_user, envelope='data')
    def get(self):
        """List all registered users"""
        all_users = get_all_users()
        print("All users=",all_users)
        return all_users

    @api.response(201, 'User successfully created.')
    @api.doc('create a new user')
    @api.expect(_user, validate=True)
    def post(self):
        """Creates a new User """
        data = request.json
        return save_new_user(data=data)


@api.route('/<public_id>')
@api.param('public_id', 'The User identifier')
@api.response(404, 'User not found.')
class User(Resource):
    @api.doc('get a user')
    @api.marshal_with(_user)
    def get(self, public_id):
        """get a user given its identifier"""
        user = get_a_user(public_id)
        if not user:
            api.abort(404)
        else:
            return user


# line 1 through 8 imports all the required resources for the user controller.
# We defined two concrete classes in our user controller which are
# userList and user. These two classes extends the abstract flask-restplus resource.
# The api namespace in line 7 above provides the controller with several decorators which includes but is not limited to the following:
# api.route: A decorator to route resources
# api.marshal_with: A decorator specifying the fields to use for serialization (This is where we use the userDto we created earlier)
# api.marshal_list_with: A shortcut decorator for marshal_with above withas_list = True
# api.doc: A decorator to add some api documentation to the decorated object
# api.response: A decorator to specify one of the expected responses
# api.expect: A decorator to Specify the expected input model ( we still use the userDto for the expected input)
# api.param: A decorator to specify one of the expected parameters