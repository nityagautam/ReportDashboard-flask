#===============================================================
# @author:  nityanarayan44@live.com
# @written: 08 December 2021
# @desc:    Backend server for the Dashboard of reports.
#===============================================================

# Import section
from flask import Flask
from app.utilites.console_animator import ConsoleAnimator


# ==============================================================
# Flask configuration
# ==============================================================
#ReportDashboard/
public_folder_path = "/public/"
public_folder_name = "public"
application = Flask(__name__, static_url_path=public_folder_path, static_folder=public_folder_name)
# Now import the route which usage the 'application' instance
import app.routes.router


# ==============================================================
# Executor
# ==============================================================
if __name__ == "__main__":
    ConsoleAnimator().print_msg_with_title(title='SERVER RE/START', msg='REPORT DASHBOARD BACKEND SERVER', dash_length=30)
    ConsoleAnimator().print_with_delay(main_string='| Initializing', loading_string='.... ', delay_time=0.2)

    if application:
        # Running the app in debug mode (modifying the source code will restart the server untill error occured)
        application.run(debug=True, host='0.0.0.0', port=10000, threaded=True) 
