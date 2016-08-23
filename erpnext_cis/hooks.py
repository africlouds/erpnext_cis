# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "erpnext_cis"
app_title = "ERPNext CIS"
app_publisher = "africlouds.com"
app_description = "ERPNext as Certified Invoicing System app"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "arwema@gmail.com"
app_license = "MIT"

fixtures = ["Custom Field",  {
	"doctype": "Print Format",
	"filters":	{
		"name": ["in", "Certified Standard"]
	}
}]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/erpnext_cis/css/erpnext_cis.css"
# app_include_js = "/assets/erpnext_cis/js/erpnext_cis.js"

# include js, css files in header of web template
# web_include_css = "/assets/erpnext_cis/css/erpnext_cis.css"
# web_include_js = "/assets/erpnext_cis/js/erpnext_cis.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "erpnext_cis.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "erpnext_cis.install.before_install"
# after_install = "erpnext_cis.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "erpnext_cis.notifications.get_notification_config"

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
	"Sales Invoice": {
		"on_submit": "erpnext_cis.ebm.certify"
	}
}
# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"erpnext_cis.tasks.all"
# 	],
# 	"daily": [
# 		"erpnext_cis.tasks.daily"
# 	],
# 	"hourly": [
# 		"erpnext_cis.tasks.hourly"
# 	],
# 	"weekly": [
# 		"erpnext_cis.tasks.weekly"
# 	]
# 	"monthly": [
# 		"erpnext_cis.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "erpnext_cis.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "erpnext_cis.event.get_events"
# }

