from . import __version__ as app_version

app_name = "core_hr"
app_title = "Core Hr"
app_publisher = "TS"
app_description = "HR Deafult feature"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "ts@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/core_hr/css/core_hr.css"
# app_include_js = "/assets/core_hr/js/core_hr.js"

# include js, css files in header of web template
# web_include_css = "/assets/core_hr/css/core_hr.css"
# web_include_js = "/assets/core_hr/js/core_hr.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "core_hr/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
doctype_list_js = {"Job Opening":"core_hr/custom/js/job_opening_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "core_hr.install.before_install"
# after_install = "core_hr.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "core_hr.uninstall.before_uninstall"
# after_uninstall = "core_hr.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "core_hr.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Employee Advance": {
		"on_submit": "core_hr.core_hr.custom.employee_advance.create_payment_entry",
	},
	"Payment Entry":{
		"on_submit":"core_hr.core_hr.custom.payment_entry.create_additional_salary"
	},
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"core_hr.tasks.all"
# 	],
# 	"daily": [
# 		"core_hr.tasks.daily"
# 	],
# 	"hourly": [
# 		"core_hr.tasks.hourly"
# 	],
# 	"weekly": [
# 		"core_hr.tasks.weekly"
# 	]
# 	"monthly": [
# 		"core_hr.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "core_hr.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "core_hr.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "core_hr.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"core_hr.auth.validate"
# ]

# Translation
# --------------------------------

# Make link fields search translated document names for these DocTypes
# Recommended only for DocTypes which have limited documents with untranslated names
# For example: Role, Gender, etc.
# translated_search_doctypes = []
