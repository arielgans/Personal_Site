from flask import Flask, redirect, url_for, render_template
from second import second

app = Flask(__name__)
app.register_blueprint(second, url_prefix="")

@app.route("/")
def home():
	return render_template("index.html")

if __name__ == "__main__":
	app.run(debug=True)