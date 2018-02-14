import game_pieces
import string

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# Test Game Rules
def test_gameRulesBaseline():
	rules = game_pieces.gameRules()
	if rules.get_letter_values() == SCRABBLE_LETTER_VALUES:
		print("SUCCESS: gameRulesBaseline()")
	else:
		print("FAILURE: gameRulesBaseline()")

# Test Letters
def test_letter():
	'''
	Unit test for letters
	'''
	rules = game_pieces.gameRules()
	letters = []
	result = [a for a in string.ascii_lowercase]
	for i in string.ascii_lowercase:
		letters.append(game_pieces.letter(game_rules = rules, character = i))
	if map(str, letters) != result:
		print("FAILURE")
	else:
		print("SUCCESS")

def test_lt():
	'''
	Unit test for less than
	'''
	rules = game_pieces.gameRules()
	a = game_pieces.letter(game_rules = rules, character = 'a')
	b = game_pieces.letter(game_rules = rules, character = 'b')
	
	if a < b:
		print("SUCCESS")
	else:
		print("FAILURE")	

def test_le():		
	'''
	Unit test for less than
	'''
	rules = game_pieces.gameRules()
	a = game_pieces.letter(game_rules = rules, character = 'a')
	b = game_pieces.letter(game_rules = rules, character = 'b')
	c = game_pieces.letter(game_rules = rules, character = 'c')
	

	if (c <= b and b <= c and a <= c and a <= b):
		print("SUCCESS")
	else:
		print("FAILURE")	

def test_gt():
	'''
	Unit test for less than
	'''
	rules = game_pieces.gameRules()
	a = game_pieces.letter(game_rules = rules, character = 'a')
	b = game_pieces.letter(game_rules = rules, character = 'b')
	c = game_pieces.letter(game_rules = rules, character = 'c')
	
	if (c > a and b > a):
		print("SUCCESS")
	else:
		print("FAILURE")	

def test_ge():	
	'''
	Unit test for less than
	'''
	rules = game_pieces.gameRules()
	a = game_pieces.letter(game_rules = rules, character = 'a')
	b = game_pieces.letter(game_rules = rules, character = 'b')
	c = game_pieces.letter(game_rules = rules, character = 'c')
	
	if (c >= b and b >= a and c >= b and b >= c):
		print("SUCCESS")
	else:
		print("FAILURE")	

def test_eq():	
	'''
	Unit test for less than
	'''
	rules = game_pieces.gameRules()
	a = game_pieces.letter(game_rules = rules, character = 'a')
	b = game_pieces.letter(game_rules = rules, character = 'b')
	c = game_pieces.letter(game_rules = rules, character = 'c')
	
	if (c == b and b == c):
		print("SUCCESS")
	else:
		print("FAILURE")	

def test_print():
	rules = game_pieces.gameRules()
	a = game_pieces.letter(game_rules = rules, character = 'a')
	b = game_pieces.letter(game_rules = rules, character = 'b')
	c = game_pieces.letter(game_rules = rules, character = 'c')
	
	print(c)



print("--------------GAME RULES---------------------------")
print("---------------------------------------------------")
print("testing gameRulesBaseline()")
test_gameRulesBaseline()

print("--------------LETTERS------------------------------")
print("---------------------------------------------------")
print("testing letter()")
test_letter()

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




print("FINISHED")
