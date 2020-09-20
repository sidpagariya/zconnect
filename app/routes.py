import flask
from app import app
import json
import app.commands as commands

global_history = []
temp_history = []

def handle_response(json_data):
    global global_history
    global temp_history
    response_message = ""
    if "is_private" in json_data:
        if "message" in json_data:
            message = json_data["message"]
            if json_data["is_private"]:
                response_message, clear_temp = commands.handle_command(message, global_history, temp_history)
                if clear_temp:
                    temp_history = []
            temp_history.append(message)
            global_history.append(message)
            print(temp_history)
            print(global_history)
            print(response_message)
    return json.dumps({
        "message": response_message
    })

@app.route('/')
def test():
    return "Hello, ZConnect!"

@app.route('/data', methods=['GET', 'POST'])
def handle_data():
    if flask.request.method == 'POST':
        json_data = json.loads(flask.request.get_json())
        print(json_data)
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