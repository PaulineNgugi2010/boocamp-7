'''Test suite for super_sum.'''

from unittest import TestCase
from super_sum import super_sum


class SuperSumTestCase(TestCase):
	'''Test case for super sum.'''
	def test_empty_input(self):
		'''Test empty input.'''
		self.assertEqual(0, super_sum())
	def test_sum_of_integers(self):
		'''Test sum of integers.'''
		self.assertEqual(super_sum(1,2,3), 6)
		self.assertEqual(super_sum(-1, 1), 0)
	def test_string_input_returns(self):
		'''Test String Inputs'''
		self.assertEqual(super_sum(''), 0)
	def test_sum_of_items_in_one_list(self):
		'''Test sum of intergers in one list'''
		self.assertEqual(super_sum([1, 2, 3]), 6)



	



