from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return {"message": "Wound Monitoring Backend Running"}

if __name__ == "__main__":
    app.run(debug=True)
