import frappe
from frappe import _
import string
import random
from frappe.utils.background_jobs import enqueue
import subprocess
import paho.mqtt.client as mqtt

def certify(doc, method):
        send_client = mqtt.Client()
        send_client.connect("192.168.56.1", 1883, 60)
        send_client.publish("SDC", "Certify %s" % doc.name)
        send_client.loop(2)
        send_client.disconnect()
