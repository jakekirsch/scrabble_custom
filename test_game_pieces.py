import game_pieces
import string
import copy

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}
TEST_LETTER_DIST = {'a': 1, 'c': 1, 'b': 1, 'e': 1, 'd': 1, 'g': 1, 'f': 1, 'i': 1, 'h': 1, 'k': 1, 'j': 1, 'm': 1, 'l': 1, 'o': 1, 'n': 1, 'q': 1, 'p': 1, 's': 1, 'r': 1, 'u': 1, 't': 1, 'w': 1, 'v': 1, 'y': 1, 'x': 1, 'z': 1}

TEST_DEFAULT_BOARD = [[['[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]'], ['[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]'], ['[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]'], ['[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]'], ['[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]'], ['[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]'], ['[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]'], ['[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]'], ['[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]'], ['[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]']]]

#TEST GAME RULES------------------------------------------------------------------------
def test_gameRulesBaseline():
	rules = game_pieces.gameRules()
	if rules.get_letter_values() == SCRABBLE_LETTER_VALUES:
		print("SUCCESS: gameRulesBaseline()")
	else:
		print("FAILURE: gameRulesBaseline()")

def test_get_letter_dist():
	'''Return letter values dict'''
	rules = game_pieces.gameRules()
	if rules.get_letter_dist() == TEST_LETTER_DIST:
		print("SUCCESS")
	else:
		print("FAILURE")
		
def test_get_board_dimension():
	'''Unit test for get_board_dimension()'''
	
	# Test 1
	rules = game_pieces.gameRules()
	if rules.get_board_dimension() == (10, 10, 1):
		print("Test 1: SUCCESS")
	else:
		print("Test 1: FAILURE")

	# Test 2
	rules = game_pieces.gameRules(board_dimension = (11, 11, 3))
	if rules.get_board_dimension() == (11, 11, 3):
		print("Test 2: SUCCESS")
	else:
		print("Test 2: FAILURE")

def test_get_board_center():
	'''Unit test for retrieving board center'''
	rules = game_pieces.gameRules()

	print(rules.get_board_center())



#TEST LETTER CLASS------------------------------------------------------------------------
def test_letter():
	'''
	Unit test for letters
	'''
	rules = game_pieces.gameRules()
	letters = []
	result = [a for a in string.ascii_lowercase]
	for i in string.ascii_lowercase:

		letters.append(game_pieces.letter(game_rules = rules, character = i))
	if list(map(str, letters)) != result:
		print("Test 1: FAILURE")
	else:
		print("Test 1: SUCCESS")

	# Test 2
	try:
		letter_Bb = game_pieces.letter(rules, 'Bb')
	except:
		print("Test 2: SUCCESS")
	else:
		print("Test 2: FAILURE")


def test_getset_owner():
	'''
	Unit test for letters - set owner
	'''
	rules = game_pieces.gameRules()
	
	# Test 1
	letter_a = game_pieces.letter(rules, 'a')
	try:
		letter_a.set_owner(1)
	except:
		print("Test 1: FAILURE")
	else:
		print("Test 1: SUCCESS")

	# Test 2
	if letter_a.get_owner() == 1:
		print("Test 2: SUCCESS")
	else:
		print("Test 2: FAILURE")

	# Test 3
	try:
		letter_a.set_owner('1')
	except:
		print("Test 3: SUCCESS")
	else:
		print("Test 3: FAILURE")


	
def test_getset_turn_id():
	'''Unit test for setting turn_id()'''
	rules = game_pieces.gameRules()
	
	# Test 1
	letter_a = game_pieces.letter(rules, 'a')

	try:
		letter_a.set_turn_id(1)
	except:
		print("Test 1: FAILURE")
	else:
		print("Test 1: SUCCESS")

	# Test 2
	letter_a = game_pieces.letter(rules, 'a')

	try:
		letter_a.set_turn_id('1')
	except:
		print("Test 2: SUCCESS")
	else:
		print("Test 2: FAILURE")

	# Test 3
	letter_a = game_pieces.letter(rules, 'a', turn_id = 1)

	if letter_a.get_turn_id() == 1:
		print("Test 3: SUCCESS")
	else:
		print("Test 3: FAILURE") 

def test_get_id_num():
	'''Unit test for get_id_num()'''
	rules = game_pieces.gameRules()
	letter_a = game_pieces.letter(rules, 'a')

	# Test 1
	try:
		letter_a.get_id_num()
	except:
		print("Test 1: FAILURE, but ok because we're making letters in other tests")
	else:
		print("Test 1: SUCCESS")

	# Test 2
	print(letter_a.get_id_num())
	if letter_a.get_id_num() == 0:
		print("Test 2: SUCCESS")
	else:
		print("Test 2: FAILURE, but ok because we're making letters in other tests")

	# Test 3

	letter_b = game_pieces.letter(rules, 'b')
	print(letter_b.get_id_num())
	if letter_b.get_id_num() == 1:
		print("Test 3: SUCCESS")
	else:
		print("Test 3: FAILURE, but ok because we're making letters in other tests")

def test_lt():
	'''
	Unit test for less than
	'''
	rules = game_pieces.gameRules()
	a = game_pieces.letter(game_rules = rules, character = 'a')
	b = game_pieces.letter(game_rules = rules, character = 'b')
	
	if a < b:
		print("Test 1: SUCCESS")
	else:
		print("Test 1:FAILURE")	

def test_le():		
	'''
	Unit test for less than
	'''
	rules = game_pieces.gameRules()
	a = game_pieces.letter(game_rules = rules, character = 'a')
	b = game_pieces.letter(game_rules = rules, character = 'b')
	c = game_pieces.letter(game_rules = rules, character = 'c')
	

	if (c <= b and b <= c and a <= c and a <= b):
		print("Test 1: SUCCESS")
	else:
		print("Test 1: FAILURE")	

def test_gt():
	'''
	Unit test for less than
	'''
	rules = game_pieces.gameRules()
	a = game_pieces.letter(game_rules = rules, character = 'a')
	b = game_pieces.letter(game_rules = rules, character = 'b')
	c = game_pieces.letter(game_rules = rules, character = 'c')
	
	if (c > a and b > a):
		print("Test 1: SUCCESS")
	else:
		print("Test 1: FAILURE")	

def test_ge():	
	'''
	Unit test for less than
	'''
	rules = game_pieces.gameRules()
	a = game_pieces.letter(game_rules = rules, character = 'a')
	b = game_pieces.letter(game_rules = rules, character = 'b')
	c = game_pieces.letter(game_rules = rules, character = 'c')
	
	if (c >= b and b >= a and c >= b and b >= c):
		print("Test 1: SUCCESS")
	else:
		print("Test 1: FAILURE")	

def test_eq():	
	'''
	Unit test for equality
	'''
	rules = game_pieces.gameRules()
	a = game_pieces.letter(game_rules = rules, character = 'a')
	b = game_pieces.letter(game_rules = rules, character = 'b')
	c = game_pieces.letter(game_rules = rules, character = 'c')
	
	if (c == b and b == c):
		print("Test 1: SUCCESS")
	else:
		print("Test 1: FAILURE")	

def test_print():
	'''Unit test for printing'''
	rules = game_pieces.gameRules()
	a = game_pieces.letter(game_rules = rules, character = 'a')
	b = game_pieces.letter(game_rules = rules, character = 'b')
	c = game_pieces.letter(game_rules = rules, character = 'c')
	
	print(c)

#TEST BAG CLASS------------------------------------------------------------------------
def test_bag():
	'''Unit test for initializing bag'''
	rules = game_pieces.gameRules()
	bag = game_pieces.bag(rules)


def test_get_letter_dict():
	'''Unit test for retrieving letter_dict'''
	rules = game_pieces.gameRules()
	bag = game_pieces.bag(rules)
	if bag.get_letter_dict() == {}:
		print("SUCCESS")
	else:
		print("FAILURE")

def test_is_empty():
	'''Unit test for is_empty()'''
	# Test 1
	rules = game_pieces.gameRules()
	bag = game_pieces.bag(rules)

	if bag.is_empty() == True:
		print("Test 1: SUCCESS")
	else:
		print("Test 1: FAILURE")

	# Test 2
	rules = game_pieces.gameRules()
	bag = game_pieces.bag(rules)
	bag.add_letters(TEST_LETTER_DIST)

	if bag.is_empty() == True:
		print("Test 1: FAILURE")
	else:
		print("Test 1: SUCCESS")


def test_number_of_letters():
	'''Unit test for returning correct number of letters'''
	rules = game_pieces.gameRules()
	
	# test 1
	bag = game_pieces.bag(rules)
	if bag.number_of_letters() == 0:
		print("Test 1: SUCCESS")
	else:
		print("Test 1: FAILURE")

	# test 2
	bag = game_pieces.bag(rules)
	bag.add_letters(TEST_LETTER_DIST)
	if bag.number_of_letters() == 26:
		print("Test 2: SUCCESS")
	else:
		print("Test 2: FAILURE")


def test_add_letters():
	'''Unit test for adding letters to the bag'''
	rules = game_pieces.gameRules()
	bag = game_pieces.bag(rules)
	bag.add_letters(TEST_LETTER_DIST)
	if (bag.get_letter_dict() == TEST_LETTER_DIST):
		print("SUCCESS")
	else:
		print("FAILURE")

def test_valid_removal():
	'''Unit test for adding letters to the bag'''
	rules = game_pieces.gameRules()
	
	# test 1
	removal_one = {'a':1, 'b':1}
	bag = game_pieces.bag(rules)
	bag.add_letters(TEST_LETTER_DIST)

	if bag.valid_removal(removal_one) == True:
		print("Test 1: SUCCESS")
	else:
		print("Test 1: FAILURE")

	# test 2
	removal_two = {}
	bag = game_pieces.bag(rules)
	bag.add_letters(TEST_LETTER_DIST)

	if bag.valid_removal(removal_two) == True:
		print("Test 2: SUCCESS")
	else:
		print("Test 2: FAILURE")	

	# test 3
	removal_three = {'a':2}
	bag = game_pieces.bag(rules)
	bag.add_letters(TEST_LETTER_DIST)

	if bag.valid_removal(removal_three) == False:
		print("Test 3: SUCCESS")
	else:
		print("Test 3: FAILURE")	
	
	# test 4
	removal_four = {'ab':1}
	bag = game_pieces.bag(rules)
	bag.add_letters(TEST_LETTER_DIST)

	if bag.valid_removal(removal_four) == False:
		print("Test 4: SUCCESS")
	else:
		print("Test 4: FAILURE")	

	# test 5
	removal_five = 'string'
	bag = game_pieces.bag(rules)
	bag.add_letters(TEST_LETTER_DIST)

	try:
		bag.valid_removal(removal_five)
		print("Test 5: FAILURE")
	except AssertionError:
		print("Test 5: SUCCESS")


def test_remove_letters():
	'''Unit test for remove letters'''
	rules = game_pieces.gameRules()
	TEST_LETTER_DIST_REMOVAL = {'a': 0, 'c': 1, 'b': 0, 'e': 1, 'd': 1, 'g': 1, 'f': 1, 'i': 1, 'h': 1, 'k': 1, 'j': 1, 'm': 1, 'l': 1, 'o': 1, 'n': 1, 'q': 1, 'p': 1, 's': 1, 'r': 1, 'u': 1, 't': 1, 'w': 1, 'v': 1, 'y': 1, 'x': 1, 'z': 1}
	
	# test 1
	removal_one = {'a':1, 'b':1}
	bag = game_pieces.bag(rules)
	bag.add_letters(TEST_LETTER_DIST)

	bag.remove_letters(removal_one)
	
	if bag.number_of_letters() == 24:
		print("Test 1: SUCCESS")
	else:
		print("Test 1: FAILURE")

	# Test 2
	if bag.get_letter_dict() == TEST_LETTER_DIST_REMOVAL:
		print("Test 2: SUCCESS")
	else:
		print("Test 2: FAILURE")

	#test 3
	removal_two = {'a': 2}
	try:
		bag.remove_letters(removal_two)
		print("Test 3: FAILURE")
	except game_pieces.bagRemovalError as error:
		print("Test 3: SUCCESS", error)

def test_give_letters():
	'''Unit test for give letters'''
	
	# Test 1 - take all letters
	rules = game_pieces.gameRules()
	bag = game_pieces.bag(rules)
	bag.add_letters(TEST_LETTER_DIST)

	if bag.give_letters(26) == TEST_LETTER_DIST:
		print("Test 1.0: SUCCESS")
	else:
		print("Test 1.0: FAILURE")
	
	if bag.is_empty():
		print("Test 1.1: SUCCESS")
	else:
		print("Test 1.1: FAILURE")


	# Test 2 - take more letters
	rules = game_pieces.gameRules()
	bag = game_pieces.bag(rules)
	bag.add_letters({'a': 1})
	
	if bag.give_letters(2) == {'a': 1}:
		print("Test 2: SUCCESS")
	else:
		print("Test 2: FAILURE")

	# Test 3 - bag is empty
	rules = game_pieces.gameRules()
	bag = game_pieces.bag(rules)
	
	if bag.give_letters(2) == {}:
		print("Test 3: SUCCESS")
	else:
		print("Test 3: FAILURE")

	# Test 4 -- Future Simulation
	print("PLACEHOLDER FOR FUTURE SIMULATION")

#GAMEBOARD-------------------------------------------------------------------
def test_board():
	'''Unit test for board init'''
	rules = game_pieces.gameRules()
	board = game_pieces.board(rules)
	print("Test 0: SUCCESS")

def test_get_dimensions():
	'''Unit test for getting board dimensions'''
	rules = game_pieces.gameRules()
	board = game_pieces.board(rules)

	if board.get_dimensions() == (10,10,1):
		print("Test 1: SUCCESS")
	else:
		print("Test 1: FAILURE")


def test_is_valid_location():
	'''Unit test for returning the 3D array, using lists'''
	rules = game_pieces.gameRules()
	board = game_pieces.board(rules)	

	# Test 1
	location_one = (1,1,1)
	try:
		board.is_valid_location(location_one)
	except:
		print("Test 1: FAILURE")
	else:
		print("Test 1: SUCCESS")

	# Test 2
	location_two = [1, 1, 1]
	try:
		board.is_valid_location(location_two)
		print("Test 2: FAILURE")
	except:
		print("Test 2: SUCCESS")
	else:
		print("Test 2: FAILURE")

	# Test 3
	location_three = ('a', 'a', 'a')
	try:
		board.is_valid_location(location_three)
		print("Test 3: FAILURE")
	except:
		print("Test 3: SUCCESS")
	else:
		print("Test 3: FAILURE")
	
	# Test 4
	location_four = ('1', 1, 1)
	try:
		board.is_valid_location(location_four)
		print("Test 4: FAILURE")
	except:
		print("Test 4: SUCCESS")
	else:
		print("Test 4: FAILURE")

	location_five = (-1, 1, 1)
	try:
		board.is_valid_location(location_five)
		print("Test 5: FAILURE")
	except:
		print("Test 5: SUCCESS")
	else:
		print("Test 5: FAILURE")


	location_six = (11, 11, 2)
	try:
		board.is_valid_location(location_six)
		print("Test 6: FAILURE")
	except:
		print("Test 6: SUCCESS")
	else:
		print("Test 6: FAILURE")


def test_is_location_empty():
	'''Unit test for checking if a slot in the board is empty'''
	rules = game_pieces.gameRules()
	board = game_pieces.board(rules)	
	
	this_board = copy.deepcopy(board)
	
	# Test 1
	location_one = (1,1,1)
	letter_a = game_pieces.letter(rules, 'a')
	this_board.add_letter(letter_a, location_one)
		
	if (this_board.is_location_empty(location_one) == False):
		print("Test 1: SUCCESS")
	else:
		print("Test 1: FAILURE")

	# Test 2
	location_one = (1,2,1)
	
	if (board.is_location_empty(location_one) == True):
		print("Test 2: SUCCESS")
	else:
		print("Test 2: FAILURE")	

def test_add_letter():
	'''Unit test for returning the 3D array, using lists'''
	rules = game_pieces.gameRules()
	board = game_pieces.board(rules)	
	
	board = copy.deepcopy(board)
	# Test 1
	location_one = (1,1,1)
	letter_a = game_pieces.letter(rules, 'a')

	print(board.get_letter_positions())
	try:		
		board.add_letter(letter_a, location_one)
	except:
		print("Test 1: FAILURE")
	else:
		print("Test 1: SUCCESS")	
		print(board.get_letter_positions())

	# Test 2
	location_two = (1,10,1)
	letter_a = game_pieces.letter(rules, 'a')
	try:
		board.add_letter(letter_a, location_two)
	except:
		print("Test 2: FAILURE")
	else:
		print("Test 2: SUCCESS")	
		print(board.get_letter_positions())

	# Test 2
	location_three = (1,4,1)
	letter_a = game_pieces.letter(rules, 'a')
	try:
		board.add_letter(letter_a, location_three)
	except:
		print("Test 3: FAILURE")
	else:
		print("Test 3: SUCCESS")	
		print(board.get_letter_positions())

def test_pretty_print_board():
	'''Unit test for pretty printing'''
	rules = game_pieces.gameRules()
	board = game_pieces.board(rules)	
	board = copy.deepcopy(board)
	
	# Test 1
	location_one = (3,1,1)
	location_two = (3,2,1)
	location_three = (1,3,1)
	location_four = (10,10,1)

	letter_a = game_pieces.letter(rules, 'a', owner = 1)
	letter_b = game_pieces.letter(rules, 'b', owner = 2)
	letter_c = game_pieces.letter(rules, 'c', owner = 1)
	letter_d = game_pieces.letter(rules, 'd', owner = 2)

	board.add_letter(letter_a, location_one)
	board.add_letter(letter_b, location_two)
	board.add_letter(letter_c, location_three)
	board.add_letter(letter_d, location_four)

	board.pretty_print_board()



def test_words_from_board():
	'''Unit test for retrieving the word from the board'''
	rules = game_pieces.gameRules()
	board = game_pieces.board(rules)
	board = copy.deepcopy(board)

	# Test 1
	location_one = (5,5,1)
	location_two = (6,5,1)
	location_three = (7,5,1)
	location_four = (8,5,1)
	location_five = (4,5,1)

	letter_a = game_pieces.letter(rules, 'h', owner = 1)
	letter_b = game_pieces.letter(rules, 'e', owner = 2)
	letter_c = game_pieces.letter(rules, 'l', owner = 1)
	letter_d = game_pieces.letter(rules, 'l', owner = 2)
	letter_e = game_pieces.letter(rules, 'o', owner = 2)

	board.add_letter(letter_a, location_five)
	board.add_letter(letter_b, location_one)
	board.add_letter(letter_c, location_two)
	board.add_letter(letter_d, location_three)
	board.add_letter(letter_e, location_four)

	board.pretty_print_board()
	board.words_from_board()

#TESTS------------------------------------------------------------------------

print("--------------GAME RULES---------------------------")
print("---------------------------------------------------")
print("testing gameRulesBaseline()")
test_gameRulesBaseline()

print("---------------------------------------------------")
print("testing get_letter_dist()")
test_get_letter_dist()

print("---------------------------------------------------")
print("testing get_board_dimension()")
test_get_board_dimension()

print("---------------------------------------------------")
print("testing get_board_center()")
test_get_board_center()

print("--------------LETTERS------------------------------")
print("---------------------------------------------------")
print("testing letter()")
test_letter()

print("---------------------------------------------------")
print("testing set_owner, get_owner()")
test_getset_owner()

print("---------------------------------------------------")
print("testing set_turn_id, get_turn_id()")
test_getset_turn_id()

print("---------------------------------------------------")
print("testing get_id_num()")
test_get_id_num()

print("---------------------------------------------------")
print("testing test_lt()")
test_lt()

print("---------------------------------------------------")
print("testing test_le()")
test_le()

print("---------------------------------------------------")
print("testing test_gt()")
test_gt()

print("---------------------------------------------------")
print("testing test_ge()")
test_ge()

print("---------------------------------------------------")
print("testing test_eq()")
test_eq()


print("---------------------------------------------------")
print("testing test_print()")
test_print()



print("--------------LETTER BAG---------------------------")
print("---------------------------------------------------")
print("testing bag()")
test_bag()

print("---------------------------------------------------")
print("testing get_letter_dict()")
test_get_letter_dict()

print("---------------------------------------------------")
print("testing number_of_letters()")
test_number_of_letters()

print("---------------------------------------------------")
print("testing is_empty()")
test_is_empty()

print("---------------------------------------------------")
print("testing add_letters()")
test_add_letters()

print("---------------------------------------------------")
print("testing valid_removal()")
test_valid_removal()

print("---------------------------------------------------")
print("testing remove_letters()")
test_remove_letters()

print("---------------------------------------------------")
print("testing give_letters()")
test_give_letters()

print("-------------BOARD---------------------------------")
print("---------------------------------------------------")
print("testing board()")
test_board()


print("---------------------------------------------------")
print("testing get_dimensions()")
test_get_dimensions()


print("---------------------------------------------------")
print("testing is_valid_location()")
test_is_valid_location()

print("---------------------------------------------------")
print("testing is_location_empty()")
test_is_location_empty()

print("---------------------------------------------------")
print("testing add_letter()")
test_add_letter()

print("---------------------------------------------------")
print("testing pretty_print_board()")
test_pretty_print_board()

print("---------------------------------------------------")
print("testing words_from_board()")
test_words_from_board()


print("FINISHED")


#