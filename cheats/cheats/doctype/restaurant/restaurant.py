# Copyright (c) 2025, BWH and contributors
# For license information, please see license.txt

# import frappe
from frappe.website.website_generator import WebsiteGenerator


class Restaurant(WebsiteGenerator):
	def before_save(self):
		self.head = "Something"
