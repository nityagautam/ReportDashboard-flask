from flask import Flask, jsonify, render_template, request
import os
import json
import argparse
import jinja2

app = Flask(__name__)


########################################
# App Gateway
########################################
@app.route('/')
def root():
    """
    Queries the snapshot data for both Serenity and JMter projects from the MongoDB.
    Renders the Snapshot view of html
    :return: N/A
    """
    # set template directory of the Flask App to the  path set by the user as command line arg.
    return '<html><head><title>Root</title><head><body><hr/> Welcome to the main page <hr/></body></html>'

@app.route('/data')
def data():
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
    #return jsonify(data)
    return json.stringify(data)


# 404 Handler; We can also pass the specific request errors codes to the decorator;
@app.errorhandler(404)
# inbuilt function which takes error as parameter
def not_found(e):
    return "<html><head><title>404</title><head><body><hr/> Oopse, page you are looking is not available right now. <hr/></body></html>", 404


# Exception/Error handler; We can also pass the specific errors to the decorator;
@app.errorhandler(Exception)
def server_error(err):
    app.logger.exception(err)
    return f"<html><head><title>500</title><head><body><hr/> Oopse, Following error occured: <br/> {err} <hr/></body></html>", 500


# Executor
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port='5000', threaded=True)  # Running the app in debug mode