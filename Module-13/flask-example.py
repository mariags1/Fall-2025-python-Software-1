import json

from flask import Flask, request, Response

app = Flask(__name__)

@app.get("/")
def hello_world():
    return "Hello, World!"

@app.get("/add")
def add_values():
    return "1 + 1"

"""""
@app.get("/sum")
def calculate_sum():
    args = request.args

    if not args.get("n1"):
        return "n1 not set"

    if not args.get("n1"):
        return "n1 not set"

    n1 = float(args.get("n1"))
    n2 = float(args.get("n2"))
    total_sum = n1 + n2

#creating dictionary
    json_data = {
       "number1": n1,
       "number2": n2,
       "total": total_sum
   }
    return json_data
"""""

@app.route("/sum/<n1>/<n2>")
def calculate_sum(n1, n2):
    args = request.args
    try:
        n1 = float(n1)
        n2 = float(n2)
        total_sum = n1 + n2

        json_data = {
            "number1": n1,
            "number2": n2,
            "total": total_sum
        }
        return json_data

    except ValueError:
        response = {
            "message": "Invalid number",
            "input": {"n1": n1, "n2": n2},
            "status": 400
        }

    json_response = json.dumps(response)
    http_response = Response(
        response = json_response,
        status = 400,
        mimetype = "application/json"
    )
    return http_response

@app.get("/echo/<text>")
def echo(text):
    return {
        "echo_data": f"{text} {text}"
    }

@app.get("/user/<id>")
def get_user(id):
    return {
        "user_id": id,
        "name": "Maria"
    }

@app.errorhandler(404)
def handle_errors(error_code):
    return "404 - oh no"

if __name__ == '__main__':
    app.run(use_reloader = True, host = "127.0.0.1", port = 5000)
