# Copyright (c) 2025, BWH and Contributors
# See license.txt

import frappe
from frappe.tests import IntegrationTestCase, UnitTestCase

# On IntegrationTestCase, the doctype test records and all
# link-field test record dependencies are recursively loaded
# Use these module variables to add/remove to/from that list
EXTRA_TEST_RECORD_DEPENDENCIES = []  # eg. ["User"]
IGNORE_TEST_RECORD_DEPENDENCIES = []  # eg. ["User"]


class UnitTestOrder(UnitTestCase):
	"""
	Unit tests for Order.
	Use this class for testing individual functions and methods.
	"""

	def setUp(self):
		self.test_customer = frappe.new_doc("Customer")
		self.test_customer.full_name = frappe.mock("name")
		self.test_customer.save()

		self.test_restaurant = frappe.new_doc("Restaurant")
		self.test_restaurant.name = "test_restaurant"
		self.test_restaurant.address = "test"
		self.test_restaurant.save()

		self.test_dish = frappe.new_doc("Dish")
		self.test_dish.title = "Rajma Chawal"
		self.test_dish.price = 10
		self.test_dish.restaurant = self.test_restaurant.name
		self.test_dish.save()

	def test_sets_total_amount_on_save(self):
		test_order = frappe.new_doc("Order")
		test_order.customer = self.test_customer.name
		test_order.restaurant = self.test_restaurant.name
		test_order.append("items", {"dish": self.test_dish.name, "price": self.test_dish.price, "qty": 2})
		test_order.save()

		self.assertEqual(test_order.total_amount, 20)

	def test_sets_child_total(self):
		test_order = frappe.new_doc("Order")
		test_order.customer = self.test_customer.name
		test_order.restaurant = self.test_restaurant.name
		test_order.append("items", {"dish": self.test_dish.name, "price": self.test_dish.price, "qty": 2})
		test_order.save()

		self.assertEqual(test_order.items[0].amount, 20)

	def tearDown(self):
		frappe.db.rollback()


class IntegrationTestOrder(IntegrationTestCase):
	"""
	Integration tests for Order.
	Use this class for testing interactions between multiple components.
	"""

	pass
