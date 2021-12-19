from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "HellS 3"

@app.route("/test")
def test():
    return "testtesttest"

if __name__=="__main__":
    app.run()