# ===[Config Starts]=================================================================

# Core configurations
core_config = {
    "preserve_reports_history_for_days": 20
}

# ===[UI Config Starts]=================================================================
app_ui_config = {
    "app_name": "AUTOMATION REPORT DASHBOARD & ANALYTICS",
    "app_poc_tag_1": "POC PROTOTYPE-1",
    "app_experimental_tag": "An @amishra's experimental",

    # Page-wise configuration data
    "about_page": {
        "title": "ABOUT",
        "desc": """This is the main page of the Automation Dashboard server. This application is to present the reports 
                more effectively and in detailed way of the executed automated suites. 
                It is just a POC(Proof of Concept) proto-type, to show-case the idea of a dashboard server 
                for better reporting of the automation reports and doing/extracting some insights from it.
                >>>>>  
                This idea came after looking at a lot of reports and jenkins execution data, 
                with an idea to represent the insights in a better way.""",
        "info": [
            "App has 3 main components:: Backend Server + FrontEnd(Aggregation and reports) + Crawler",
            "Server is written on 'Python3' with 'Flask'", 
            "Frontend is written using Javascript/HTML/CSS/ using Jinja Templating engine ",
            "Crawler is the data extractor from the HTML/XML/JSON reports (Being written on Python3)",
            "crawler may/may not be added as a trigger on CI/CD so that once any build get done, crawler should be triggered as a POST-ACTION.",
            "they(Crawlers) can also be triggerd independently."
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
            "name": "ANALYTICS",
            "route": "/analytics",
            "icon": "fa fa-bar-chart fa-lg fa-fw"
        },
        {"name": "-", "route": "-", "icon": "-"},
        {"name": "-", "route": "-", "icon": "-"},
        {"name": "-", "route": "-", "icon": "-"},
        {"name": "-", "route": "-", "icon": "-"},
        
        {
            "name": "NOTES",
            "route": "/notes",
            "icon": "fa fa-newspaper-o fa-lg fa-fw"
        },
        {
            "name": "ABOUT",
            "route": "/about",
            "icon": "fa fa-book"
        }
    ]
    # End of side menu
}
"""
Side Bar menu junk
,
        {
            "name": "HISTORY",
            "route": "/history",
            "icon": "fa fa-history fa-lg fa-fw"
        },
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
"""
# ===[UI Config Ends]===================================================================
