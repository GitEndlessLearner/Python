def get_formatted_name(first, last):
	"""Generate a neatly formatted full name."""
	full_name = first + ' ' + last
	return full_name.title()

"""
print("Enter 'q' at any time to quit.")
while True:
	first = input("\nPlease give me a first name:\n")
	if first == 'q':
		break
	last = input("\nPlease give me a last name:\n")
	if last == 'q':
		break

formatted_name = get_formatted_name(first, last)
print("\tNeatly formatted name: " + formatted_name + '.')
"""

import unittest

class NamesTestCase(unittest.TestCase):
	"""测试"""

	def test_first_last_name(self):
		"""是否能正确处理Janis 是否能正确处理Janis Joplin这样的姓名吗"""
		formatted_name = get_formatted_name('janis', 'joplin')
		self.assertEqual(formatted_name, 'Janis Joplin')
 
unittest.main()


"""
常用的断言
assertEqual(a,b) 核实a==b
assertNotEqual(a,b) 核实a!=b
assertTrue(x) 核实x为True
assertFalse(x) 核实x为False
assertIn(item,list) 核实item在List中
assertNotIn(item,list) 核实item不在List中

ToBeContinue······

"""


