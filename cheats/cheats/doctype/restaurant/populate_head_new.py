import frappe

def execute():
    frappe.db.set_value("Restaurant", {}, "head", "NA")
