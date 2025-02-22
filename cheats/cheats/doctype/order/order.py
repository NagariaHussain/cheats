# Copyright (c) 2025, BWH and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Order(Document):
	def validate(self):
		self.total_amount = 0

		for item in self.items:
			item.amount = item.qty * item.price
			self.total_amount += item.amount

