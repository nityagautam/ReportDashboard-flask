#===============================================================
# @author:  nityanarayan44@live.com
# @written: 08 December 2021
# @desc:    Routes for the Backend server
#===============================================================

# Import section with referecne of entry file or main file;
from __main__ import application
from flask import jsonify, render_template, url_for, request, redirect
# Local sample data import
from app.config.uiconfig import app_ui_config
from app import sample_data


# ==============================================================
# App Routes/Gateways
# ==============================================================
@application.route('/test', methods=['GET'])
def test():
    return '<h4>HELLO WORLD!</h4><hr/> it works!'

@application.route('/', methods=['GET'])
@application.route('/home', methods=['GET'])
@application.route('/dashboard', methods=['GET'])
def root():
    return render_template("dashboard.html", app_data=app_ui_config, data=sample_data.latest_data)


@application.route('/history', methods=['GET'])
def history():
    return render_template("history.html", app_data=app_ui_config, data=sample_data.history_data)


@application.route('/about', methods=['GET'])
def about():
    return render_template("about.html", app_data=app_ui_config, data=sample_data.latest_data)


@application.route('/get-notes', methods=['POST'])
def get_todo():
    print("KEY :: VALUE (from the received form data)")
    print([(key, val) for key, val in zip(request.form.keys(), request.form.values())])
    return redirect("/notes", code=302)


@application.route('/notes')
def info():
    return render_template("notes.html", app_data=app_ui_config)
 

@application.route('/sample-data')
def get_sample_data():
    return jsonify(app_ui_config)

    
# ==============================================================
# Error Handlers Starts
# ==============================================================
# 404 Handler; We can also pass the specific request errors codes to the decorator;
@application.errorhandler(404)
def not_found(err):
    return render_template("error.html", app_data=app_ui_config, error_data=err), 400


# Exception/Error handler; We can also pass the specific errors to the decorator;
@application.errorhandler(TypeError)
def server_error(err):
    application.logger.exception(err)
    return render_template("error.html", app_data=app_ui_config, error_data=err), 500


# Exception/Error handler; We can also pass the specific errors to the decorator;
@application.errorhandler(Exception)
def server_error(err):
    application.logger.exception(err)
    return render_template("error.html", app_data=app_ui_config, error_data=err), 500
# ==============================================================
# Error Handlers Ends
# ==============================================================

# Route For Sample data
@application.route('/data')
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

# ==============================================================
# Extra routes starts
# ==============================================================
@application.route('/sample1')
def sample1():
    return render_template("web-analytics-overview.html")


@application.route('/sample2')
def sample2():
    return render_template("web-analytics-real-time.html")


@application.route('/logo')
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

