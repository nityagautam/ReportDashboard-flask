# This is just a imitation of mongo database
# 'reports' is the collection name
# that contains many records/documents related to the report

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
