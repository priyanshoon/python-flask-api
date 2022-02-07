try:
    from api.controller.views import LoginController
    from flask import Flask, request
    from flask_restful import Resource, Api, reqparse
except Exception as e:
    print(f"Error in loading... {e}")

app = Flask(__name__)
api = Api(app)

