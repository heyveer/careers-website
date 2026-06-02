#from flask module import Flask class
from flask import Flask

app = Flask(__name__)
print(app)

@app.route("/")
def hello_world():
    return "Hello, Flask world!!xx"

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug = True)