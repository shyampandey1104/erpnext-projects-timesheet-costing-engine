# Copyright (c) 2026, Shyamkumar Pandey and contributors
# For license information, please see license.txt

app_name = "projects_costing"
app_title = "Erpnext Projects Timesheet Costing Engine"
app_publisher = "Shyamkumar Pandey"
app_description = "Erpnext Projects Timesheet Costing Engine for Frappe and ERPNext"
app_email = "shyampandey1104@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------
app_include_css = "/assets/projects_costing/css/projects_costing.bundle.css"
app_include_js = "/assets/projects_costing/js/projects_costing.bundle.js"

# Document Events
# ---------------
doc_events = {
    "DocType Event": {
        "on_submit": "projects_costing.engine.on_document_submit",
        "on_cancel": "projects_costing.engine.on_document_cancel"
    }
}

# Scheduled Tasks
# ---------------
scheduler_events = {
    "daily": [
        "projects_costing.engine.daily_scheduled_sync"
    ]
}
