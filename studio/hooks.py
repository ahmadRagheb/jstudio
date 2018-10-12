# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "studio"
app_title = "Studio"
app_publisher = "Maxwell Morais"
app_description = "Frappe Studio"
app_icon = "octicon octicon-light-bulb"
app_color = "gold"
app_email = "max.morais.dmm@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/studio/css/studio.css"
app_include_js = "/assets/studio/js/studio.js"

# include js, css files in header of web template
# web_include_css = "/assets/studio/css/studio.css"
# web_include_js = "/assets/studio/js/studio.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
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

# Website user home page (by function)
# get_website_user_home_page = "studio.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "studio.install.before_install"
# after_install = "studio.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "studio.notifications.get_notification_config"

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

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
 	"*": {
 		"onload": "studio.api.run_event",
		"before_naming": "studio.api.run_event",
		"autoname": "studio.api.run_event",
		"validate": "studio.api.run_event",
		"before_save": "studio.api.run_event",
		"after_save": "studio.api.run_event",
		"before_insert": "studio.api.run_event",
		"after_insert": "studio.api.run_event",
		"before_submit": "studio.api.run_event",
		"after_submit": "studio.api.run_event",
		"on_update": "studio.api.run_event",
		"on_submit": "studio.api.run_event",
		"on_cancel": "studio.api.run_event",
		"on_update_after_submit": "studio.api.run_event",
		"on_change": "studio.api.run_event",
		"on_trash": "studio.api.run_event",
		"after_delete": "studio.api.run_event"
	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"studio.tasks.all"
# 	],
# 	"daily": [
# 		"studio.tasks.daily"
# 	],
# 	"hourly": [
# 		"studio.tasks.hourly"
# 	],
# 	"weekly": [
# 		"studio.tasks.weekly"
# 	]
# 	"monthly": [
# 		"studio.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "studio.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
override_whitelisted_methods = {
 	'frappe.desk.query_report.run': 'studio.api.query_report_run'
}

studio_functions = [
	'frappe._',
	'frappe.as_json',
	'frappe.msgprint',
	{'frappe.call': 'studio.functions.call'},
	{'frappe.db.get_value': 'studio.functions.get_value'},
	{'frappe.db.exists': 'studio.functions.exists'},
	{'frappe.db.count': 'studio.functions.count'},
	{'frappe.db.sql': 'studio.functions.run_sql'},
	{'frappe.model.get_list': 'frappe.client.get_list'},
	{'frappe.model.get_count': 'frappe.client.get_count'},
	{'frappe.model.count': 'frappe.client.get_count'},
	{'frappe.model.get': 'frappe.client.get_value'},
	{'frappe.model.get_value': 'frappe.client.get_value'},
	{'frappe.model.get_single_value': 'frappe.client.get_single_value'},
	{'frappe.model.set_value': 'frappe.client.set_value'},
	{'frappe.model.insert': 'frappe.client.insert'},
	{'frappe.model.insert_many': 'frappe.client.insert_many'},
	{'frappe.model.save': 'frappe.client.save'},
	{'frappe.model.rename_doc': 'frappe.client.rename_doc'},
	{'frappe.model.submit': 'frappe.client.submit'},
	{'frappe.model.cancel': 'frappe.client.cancel'},
	{'frappe.model.delete': 'frappe.client.delete'},
	{'frappe.model.set_default': 'frappe.client.set_default'},
	{'frappe.model.bulk_update': 'frappe.client.bulk_update'},
	{'frappe.model.has_permission': 'frappe.client.has_permission'},
	'frappe.utils',
	{'frappe.get_url': 'frappe.utils.get_url'},
	{'frappe.api_client': 'frappe.frappeclient'},
	{'frappe.web': 'studio.functions.web'},
	'frappe.format_value',
	{'frappe.form_dict': 'studio.functions.form_dict'},
	'frappe.get_hooks',
	{'frappe.get_doc': 'studio.functions.get_doc'},
	'frappe.new_doc',
	'frappe.get_list',
	'frappe.get_all',
	{'frappe.attach_file': 'frappe.client.attach_file'},
	{'frappe.user': 'studio.functions.user'},
	{'frappe.get_fullname': 'frappe.utils.get_fullname'},
	{'frappe.get_gravatar': 'frappe.utils.get_gravatar'},
	'frappe.render_template',
]

studio_library_path = [
	'studio/libraries'
]