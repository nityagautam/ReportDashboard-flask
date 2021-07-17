from flask import Flask, send_from_directory, render_template, request
import os
import argparse
import jinja2

# Take the flask instance
# ============================
app = Flask(__name__)


# Server Routers
# ============================
@app.route('/')
def main_entry():
    # return render_template("sample.html", test_data={"key1": "value1"})
    return '<html><head><title>Entry</title><head><body><hr/> Hello world <hr/></body></html>'


@app.route('/history/<string:project_name>')
def project_history(project_name):
    pass


@app.route('/settings')
def settings():
    pass


@app.route('/notfound')
def page_not_found():
    pass


# Execution starts from here
# ============================
if __name__ == "__main__":
    '''
    Parsing the command line arguments
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument("-td", "--template_dir", help="Location for Template", required='True')
    parser.add_argument("-hp", "--hidden_project", help='List of projects we want to hide')
    args = parser.parse_args()

    my_loader = jinja2.ChoiceLoader([app.jinja_loader, jinja2.FileSystemLoader([temp_dir[0], temp_dir[1]]), ])
    app.jinja_loader = my_loader
    app.run(debug=True, host='0.0.0.0', threaded=True)  # Running the app in debug mode
