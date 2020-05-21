from flask import request
from flask_restx import Resource

from ..util.dto import BlogsDto
from ..service.blogs_service import save_new_blogs, get_all_blogss, get_a_blogs

api = BlogsDto.api
_blogs = BlogsDto.blogs


@api.route('/')
class blogsList(Resource):
    @api.doc('list_of_registered_blogss')
    # @api.marshal_list_with(_blogs, envelope='data')
    def get(self):
        """List all registered blogss"""
        all_blogss = get_all_blogss()
        print("All blogss=",all_blogss)
        return all_blogss

    @api.response(201, 'blogs successfully created.')
    @api.doc('create a new blogs')
    @api.expect(_blogs, validate=True)
    def post(self):
        """Creates a new blogs """
        data = request.json
        return save_new_blogs(data=data)


@api.route('/<public_id>')
@api.param('public_id', 'The blogs identifier')
@api.response(404, 'blogs not found.')
class blogs(Resource):
    @api.doc('get a blogs')
    @api.marshal_with(_blogs)
    def get(self, public_id):
        """get a blogs given its identifier"""
        blogs = get_a_blogs(public_id)
        if not blogs:
            api.abort(404)
        else:
            return blogs


# line 1 through 8 imports all the required resources for the blogs controller.
# We defined two concrete classes in our blogs controller which are
# blogsList and blogs. These two classes extends the abstract flask-restplus resource.
# The api namespace in line 7 above provides the controller with several decorators which includes but is not limited to the following:
# api.route: A decorator to route resources
# api.marshal_with: A decorator specifying the fields to use for serialization (This is where we use the blogsDto we created earlier)
# api.marshal_list_with: A shortcut decorator for marshal_with above withas_list = True
# api.doc: A decorator to add some api documentation to the decorated object
# api.response: A decorator to specify one of the expected responses
# api.expect: A decorator to Specify the expected input model ( we still use the blogsDto for the expected input)
# api.param: A decorator to specify one of the expected parameters