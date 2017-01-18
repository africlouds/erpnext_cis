import frappe
from frappe import _
import string
import random
from frappe.utils.background_jobs import enqueue
import subprocess
from pubnub import Pubnub
 

pubnub = Pubnub(publish_key="pub-c-ef89b3d0-f24a-41d1-a433-23e197c0d118", subscribe_key="sub-c-23be2166-d597-11e6-bd29-0619f8945a4f")



def create_certification_task(doc, method):
	selected_sdc = select_sdc()
	frappe.get_doc({
		"doctype": "Certification Task", 
		"invoice": doc.name,
		"sdc": selected_sdc.name
	}).insert()


def select_sdc():
	filters = {
		'status':'Free'
	}
	all_sdc = frappe.get_list("SDC", filters=filters, fields=['name'])
	return all_sdc[0]

def send_task_notification(doc, method):
	task = frappe.get_doc("Certification Task", doc.name)
	pubnub.publish(channel=task.sdc, message="Certify %s" % task.invoice)



