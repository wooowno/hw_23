from flask import Flask, request, jsonify
from flask_restx import Resource, Api

from functions import *

app = Flask(__name__)

api = Api(app)
perform_ns = api.namespace("")

commands = {
    'filter': filter_lines,
    'map': map_lines,
    'unique': unique_lines,
    'sort': sort_lines,
    'limit': limit_lines
}


@perform_ns.route("/perform_query")
class PerformView(Resource):
    def post(self):
        req_json = request.json
        filename = req_json.get('file_name')
        cmd1 = req_json.get('cmd1')
        value1 = req_json.get('value1')
        cmd2 = req_json.get('cmd2')
        value2 = req_json.get('value2')

        try:
            data = file_data(filename)
        except FileNotFoundError as e:
            return "Файл не найден"

        try:
            command1 = commands[cmd1]
            command2 = commands[cmd2]
        except KeyError as e:
            return "Команда не найдена"

        data = command1(data, value1)
        data = command2(data, value2)

        data = list(data)

        return jsonify({'result': data})


if __name__ == '__main__':
    app.run()

