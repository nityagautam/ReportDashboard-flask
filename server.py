from flask import Flask
from flask import jsonify
from flask import render_template
from flask import url_for
import os
import json
import argparse
import jinja2
import sample_data

# ==============================================================
# Flask configuration
# ==============================================================
public_folder_path = "/ReportDashboard/public/"
public_folder_name = "public"
app = Flask(__name__, static_url_path=public_folder_path, static_folder=public_folder_name)


# ==============================================================
# App Routes/Gateways
# ==============================================================
@app.route('/')
@app.route('/home')
def root():
    return render_template("index.html", data=sample_data.projects)


@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html", data=sample_data.letest_data)


@app.route('/history')
def history():
    return render_template("history.html", data=sample_data.letest_data)


@app.route('/analytics')
def analytics():
    return render_template("analytics.html", data=sample_data.letest_data)


@app.route('/crawler-history')
def crawler_history():
    return "<h4> NOT AVAILABLE </h4>"

# ==============================================================
# Extra routes starts
# ==============================================================
@app.route('/sample1')
def sample1():
    return render_template("web-analytics-overview.html")


@app.route('/sample2')
def sample2():
    return render_template("web-analytics-real-time.html")


@app.route('/logo')
def get_logo():
    """
    Queries the snapshot data for both Serenity and JMeter projects from the MongoDB.
    Renders the Snapshot view of html
    :return: N/A
    """
    # set template directory of the Flask App to the  path set by the user as command line arg.
    return f'<html><head><title>Root</title><head><body><hr/> Welcome to the main page <hr/> ' \
           f'Building image from static public location: <br/> ' \
           f'<img src=\'{url_for("static", filename="images/logo.svg")}\' /> </body></html>'


@app.route('/data')
def get_data():
    data = {
        "reports": [
            {
                "build": "build_no",
                "created": "Imported 05052021T11:30:00:00IST",
                "platform": "Imported Win/Unix/Mac",
                "project_name": "project_name_1",
                "report_location_path": "path/to/report/location/index.html",
                "report_summary": {"pass": "50", "fail": "0", "ignored": "0", "skipped": "0"},
                "total_time": "35 min."
            },
            {
                "build": "build_no",
                "created": "Imported 05052021T11:30:00:00IST",
                "platform": "Imported Win/Unix/Mac",
                "project_name": "project_name_2",
                "report_location_path": "path/to/report/location/index.html",
                "report_summary": {"pass": "10", "fail": "2", "ignored": "0", "skipped": "0"},
                "total_time": "0.2345 secs."
            },
            {
                "build": "build_no",
                "created": "Imported 05052021T11:30:00:00IST",
                "platform": "Imported Win/Unix/Mac",
                "project_name": "project_name_3",
                "report_location_path": "path/to/report/location/index.html",
                "report_summary": {"pass": "100", "fail": "5", "ignored": "0", "skipped": "0"},
                "total_time": "5 days"
            }
        ]
    }
    return jsonify(data)


@app.route('/error')
def get_error():
    # It will throw an error
    d = {1: True, 2: False}
    json.dumps(d)
    return json.stringify(d)
# ==============================================================
# Extra routes ends
# ==============================================================


# ==============================================================
# Error Handlers Starts
# ==============================================================
# 404 Handler; We can also pass the specific request errors codes to the decorator;
@app.errorhandler(404)
# inbuilt function which takes error as parameter
def not_found(err):
    return "<html><head><title>404</title><head><body><hr/> Oops, page you are looking is not available right now. " \
           f"<hr/> Error: {err} </body></html>", 404


# Exception/Error handler; We can also pass the specific errors to the decorator;
@app.errorhandler(Exception)
def server_error(err):
    app.logger.exception(err)
    return f"<html><head><title>500</title><head><body><hr/> Oops, Following error occurred: <br/> {err} " \
           f"<hr/></body></html>", 500
# ==============================================================
# Error Handlers Ends
# ==============================================================


# ==============================================================
# Executor
# ==============================================================
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=10000, threaded=True)  # Running the app in debug mode
