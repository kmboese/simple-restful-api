from user_api import users
from flask_restful import Api, Resource, reqparse

from http_codes import *


class UserFunctions(Resource):
    def get(self):
        if len(users) > 0:
            return users, HTTP_OK
        else:
            return "No users found", HTTP_NOT_FOUND