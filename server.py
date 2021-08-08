from flask import Flask, jsonify, render_template, request, url_for
import os
import json
import argparse
import jinja2
import sample_data
# Flask configuration
public_folder_path = "/ReportDashboard/public/"
public_folder_name = "public"
app = Flask(__name__, static_url_path=public_folder_path, static_folder=public_folder_name)


########################################
# App Gateway
########################################
@app.route('/')
def home():
    # sample_data.data = [
    #         {
    #             "key": "Well, I came from flask server",
    #             "project_name": "Project Alpha-1",
    #             "build_no": "build15",
    #             "build_url": "https://jenkins.url/prj/build15",
    #             "report_date": "1 Aug 2021",
    #             "crawled_date": "10 Aug 2021",
    #             "report_location": "https://some.path/prj/build15/index.html",
    #             "test_result": {
    #                 "labels": ["Pass", "Fail", "Error", "Skipped", "Ignored"],
    #                 "values": [10, 9, 8, 7, 6]
    #             }
    #         }
    # ]
    #
    return render_template("index.html", data=sample_data.data)


@app.route('/root')
def root():
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


# Executor
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=10000, threaded=True)  # Running the app in debug mode
