from flask_restful import Api, Resource, reqparse
from http_codes import *
from messages import *

# Create a list of local users (actually get this info from a database)
users = {
    'Nicholas': {
        'name': 'Nicholas',
        'age': 42,
        'occupation': 'Network Engineer'
    },
    'Elvin': {
        'name': 'Elvin',
        'age': 32,
        'occupation': 'Doctor'
    },
    'Jass': {
        'name': 'Jass',
        'age': 22,
        'occupation': 'Web Developer'
    }
}

# RESTful endpoint to get user data
class User(Resource):
    def get(self, name):

        # Attempt to retrieve user
        if users.get(name):
            return users[name], HTTP_OK
            
        # Handle user not found
        else:
            return USER_NOT_FOUND_MSG, HTTP_NOT_FOUND

    def post(self, name):
        global users

        parser = reqparse.RequestParser()
        parser.add_argument('age')
        parser.add_argument('occupation')
        args = parser.parse_args()
        
        # Check if user already exists
        if users.get(name) is not None:
            return 'User with name {} already exists'\
                .format(name), HTTP_BAD_REQUEST

        # Otherwise, create the user
        user = {
            'name': name,
            'age': args['age'],
            'occupation': args['occupation']
        }
        key = user['name']
        users[key] = user
        return user, HTTP_CREATED

    def put(self, name):
        global users 

        parser = reqparse.RequestParser()
        parser.add_argument('age')
        parser.add_argument('occupation')
        args = parser.parse_args()

        # If user doesn't exist, create the user
        user = {
                'name': name,
                'age': args['age'],
                'occupation': args['occupation']
            }
        if users.get(name) is None:
            key = user['name']
            users[key] = user
            return user, HTTP_CREATED
        
        # Else, update the user
        users[name] = user
        return user, HTTP_OK

    def delete(self, name):
        global users

        if users.get(name):
            users.pop(name)
            return '{} has been deleted.'.format(name), HTTP_OK

        else:
            return USER_NOT_FOUND_MSG, HTTP_NOT_FOUND
