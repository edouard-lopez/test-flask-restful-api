from flask import Flask, Response, request
from flask_restful import Api, Resource, abort

app = Flask(__name__)
api = Api(app, prefix='/api')

class Root(Resource):
    def get(self):
        return {
                'results': None
                }

api.add_resource(Root, '/')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
