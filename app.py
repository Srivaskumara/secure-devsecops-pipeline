from flask import Flask , request
import os 

AWS_ACCESS_KEY = "AKIAIOSFODNN7EXAMPLE"

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