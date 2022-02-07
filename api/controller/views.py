try:
    import os
    import jwt
    import json
    import datetime
    from flask import app, Flask, request
    from flask_httpauth import HTTPBasicAuth
    from flask_restful import Resource, Api, reqparse
except Exception as e:
    print(f"Error {e}")

app = Flask(__name__)
api = Api(app)
auth = HTTPBasicAuth()
app.config['SECRETE_KEY'] = '15524F3915709BB42CD757FDA174694DD5A4948301B6874F79884FCD1129F4FF'

USER_DATA = {
    "admin": "admin"
}


@auth.verify_password
def verify(username, password):
    if not (username, password):
        return False
    return USER_DATA.get(username) == password


class LoginController(Resource):
    def __init__(self):
        self.name = parser.parse_args().get("name", None)

    @auth.login_required
    def get(self):
        return "Hello, World!", 200


parser = reqparse.RequestParser()
parser.add_argument('name', type=str, required=True, help='name [str] Query Param Required')
