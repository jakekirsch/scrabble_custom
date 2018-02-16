# Scrabble 3D
# ------------------------------------------

# Author: Jake Kirsch
# Module: Test Suite for helper_functions.py
import helper_functions

def test_list_to_dict():
	'''
	Unit test for list_to_dict()
	'''

	# Test 1
	dict_1 = {'a':3}
	list_1 = ['a', 'a', 'a']
	if helper_functions.list_to_dict(list_1) == dict_1:
		print("Test 1: SUCCESS")
	else:
		print("Test 1: FAILURE")

	# Test 2
	dict_2 = {}
	list_2 = []
	if helper_functions.list_to_dict(list_2) == dict_2:
		print("Test 2: SUCCESS")
	else:
		print("Test 2: FAILURE")

	# Test 3
	dict_3 = {'a': 2}
	list_3 = [1, 2]
	
	try:
		helper_functions.list_to_dict(list_3)
	except AssertionError:
		print("Test 3: SUCCESS")
	else:
		print("Test 3: FAILURE")

	# Test 4
	dict_4 = {'a': 2}
	try:
		helper_functions.list_to_dict(dict_4)
	except AssertionError:
		print("Test 4: SUCCESS")
	else:
		print("Test 4: FAILURE")




def test_dict_to_list():
	'''
	Unit test for dict_to_list()
	'''
	# Test 1
	dict_1 = {'a':3, 'b': 1}
	list_1 = ['b', 'a', 'a', 'a']

	if sorted(helper_functions.dict_to_list(dict_1)) == sorted(list_1):
		print("Test 1: SUCCESS")

	else:
		print("Test 1: FAILURE")

	# Test 2
	dict_2 = {}
	list_2 = []
	if sorted(helper_functions.dict_to_list(dict_2)) == sorted(list_2):
		print("Test 2: SUCCESS")
	else:
		print("Test 2: FAILURE")

	# Test 3
	dict_3 = {1: 'a'}
	list_3 = [1, 2]
	
	try:
		helper_functions.dict_to_list(dict_3)
	except AssertionError:
		print("Test 3: SUCCESS")
	else:
		print("Test 3: FAILURE")

	# Test 5
	list_4 = ['a', 'b']

	try:
		helper_functions.dict_to_list(list_4)
	except AssertionError:
		print("Test 4: SUCCESS")
	else:
		print("Test 4: FAILURE")


#------------------------------------------------------------------------

print("--------------HELPER FUNCTIONS---------------------")
print("---------------------------------------------------")
print("testing list_to_dict()")
test_list_to_dict()


print("---------------------------------------------------")
print("testing dict_to_list()")
test_dict_to_list()
