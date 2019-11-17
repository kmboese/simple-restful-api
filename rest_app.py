from flask import Flask
from flask_restful import Api, Resource, reqparse
 # import the user class and the list of users
from users import User, users       
from user_functions import UserFunctions

# Dev flags
DEBUG = True

def main():
    app = Flask(__name__)
    api = Api(app)

    # Add the User resource to our API
    api.add_resource(User, "/user/<string:name>")

    # Add getUsers resource to API
    api.add_resource(UserFunctions, "/users")

    # Run the app in Debug mode if specified
    app.run(debug=DEBUG)

if __name__ == "__main__":
    main()