import frappe

import erpnext
from erpnext.tests.utils import LiwaERPTestSuite


@erpnext.allow_regional
def test_method():
	return "original"


class TestInit(LiwaERPTestSuite):
	def test_regional_overrides(self):
		frappe.flags.country = "Maldives"
		self.assertEqual(test_method(), "original")
