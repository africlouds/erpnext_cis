import frappe
from frappe import _
import string
import random
from frappe.utils.background_jobs import enqueue
import subprocess

def certify(doc, method):
	invoice = frappe.get_doc("Sales Invoice", doc.name)
	invoice.receipt_number = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
	invoice.internal_data = "bbbbbbbbbbbbbbbbbbbbbbbbbbbbb"
	invoice.receipt_signature = "ssssssssssssssssssssssssssss"
	invoice.receipt_signature = "ssssssssssssssssssssssssssss"
	invoice.save()
	frappe.db.commit()
