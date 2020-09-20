import flask
from app import app
import json
import commands

def handle_response(json_data):
    if "is_private" in json_data:
        if "message" in json_data:
            message = json_data["message"]
            response_message = commands.handle_command(message)
            if response_message:
                return json.dumps({
                    "message": response_message
                })
    return ""

# from commands import *
@app.route('/')
def test():
    return "Hello, ZConnect!"

@app.route('/data', methods=['GET', 'POST'])
def handle_data():
    if flask.request.method == 'POST':
        json_data = flask.request.get_json()
        return handle_response(json_data)
    return ""

# @app.route('/webhook', methods=['POST'])
# def handle_request():
#     print(request.data)
#     json_data = flask.request.json
#     slash = json_data["name"]
#     if slash is "anon":
#         anon(json_data)
#     else:
#         pass
#     return "Request received"