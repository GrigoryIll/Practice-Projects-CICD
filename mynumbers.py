import random
from flask import Flask

app = Flask(__name__)


def numbers():
    mynumbers = [random.randint(0, 10) for _ in range(5)]
    return mynumbers


@app.route("/")
def hello_world():
    return str(numbers())


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=80)
