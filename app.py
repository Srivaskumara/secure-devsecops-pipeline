from flask import Flask , request
import os 

GITHUB_TOKEN = "ghp_12345678901234567890123455"

app = Flask(__name__)

@app.route("/")
def home():
    return "Secure DevSecOps Pipeline is running!"

@app.route("/run")
def run_command():
    cmd=request.args.get("cmd")
    return os.popen(cmd).read()


if __name__== "__main__":
    app.run(host="0.0.0.0", port=5000)