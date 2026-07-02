from flask import Flask 

AWS_ACCESS_KEY="AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_ACCESS_KEY="wJaIrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

app = Flask(__name__)

@app.route("/")
def home():
    return "Secure DevSecOps Pipeline is running!"

if __name__== "__main__":
    app.run(host="0.0.0.0", port=5000)