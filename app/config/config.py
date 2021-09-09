# ===[Config Starts]=================================================================

# Core configurations
core_config = {
    "preserve_reports_history_for_days": 20
}

# UI related configurations
ui_config = {
    "app_name": "DASHBOARD & ANALYTICS",
    "app_poc_tag_1": "POC PROTOTYPE-1",
    "app_experimental_tag": "@amishra's Experimental",

    # Page-wise configuration data
    "about_page": {
        "title": "ABOUT THIS APPLICATION",
        "desc": """This is the main page of the Automation Dashboard server. This application is to present the reports 
                more effectively and in detailed way of the executed automated suites. 
                It is just a POC(Proof of Concept) proto-type, to show-case the idea of a dashboard server 
                for better reporting of the automation reports and doing/extracting some insights from it.
                >>>>>  
                This idea took place on Aug 2021 after seeing a lot of reports and jenkins data, with an idea to 
                represent the insights in a better way.""",
        "info": [
            "App has 3 main components:: Server + Data Manager(Aggregation and reports) + Crawler",
            "Server is written on 'Python3' and has 'Flask' + 'Jinja Templates (for views)' ",
            "Data Manager manages the html reports on disk (Being written on Python3 + Sqlite3)",
            "Crawler is the data extractor from the HTML/XML/JSON reports (Being written on Python3)",
            "crawler should/must add a trigger on CI/CD so that once any build get done, crawler should be triggered.",
        ]
    },
    "dashboard_page": {
        "title": "OVERALL DASHBOARD"
    },
    "history_page": {
        "title": "OVERALL EXECUTION HISTORY FOR PROJECTS"
    },
    "analytics_page": {
        "title": "PROJECT ANALYTICS"
    },
    "crawl_history_page": {
        "title": "PROJECT CRAWLING HISTORY"
    },
    "settings_page": {
        "title": "SETTINGS"
    },
    "notes_page": {
        "title": "NOTES"
    },

    # Side Menus
    "side_menu": [
        {
            "name": "DASHBOARD",
            "route": "/dashboard",
            "icon": "fa fa-dashboard fa-lg fa-fw"
        },
        {
            "name": "HISTORY",
            "route": "/history",
            "icon": "fa fa-history fa-lg fa-fw"
        },
        {
            "name": "ANALYTICS",
            "route": "/analytics",
            "icon": "fa fa-bar-chart fa-lg fa-fw"
        },
        {"name": "-", "route": "-", "icon": "-"},
        {"name": "-", "route": "-", "icon": "-"},
        {"name": "-", "route": "-", "icon": "-"},
        {"name": "-", "route": "-", "icon": "-"},
        {
            "name": "CRAWL HISTORY",
            "route": "/crawl_history",
            "icon": "fa fa-clock-o fa-lg fa-fw"
        },
        {
            "name": "SETTINGS",
            "route": "/settings",
            "icon": "fa fa-gear fa-lg fa-fw"
        },
        {
            "name": "NOTES",
            "route": "/notes",
            "icon": "fa fa-newspaper-o fa-lg fa-fw"
        },
        {
            "name": "ABOUT",
            "route": "/about",
            "icon": "fa fa-home fa-lg fa-fw"
        }
    ]
    # End of side menu
}
# ===[Config Ends]===================================================================
