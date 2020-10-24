# Flask
import os
from flask import Flask, jsonify, request, abort, redirect, url_for, render_template
# Custom
from second import second
from AutoResume import AutoResumeObject

app = Flask(__name__)
app.register_blueprint(second, url_prefix="")

@app.route("/")
@app.route("/projects/")
def home():
	return render_template("projects.html")

@app.route("/get-gsheet-data/", methods=["GET"])
def get_gsheet_data():
	dataGetter = AutoResumeObject()
	return jsonify(dataGetter.display_all())

if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True, port=os.environ.get('PORT', 80))