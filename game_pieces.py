# Scrabble 3D
# ------------------------------------------

# Author: Jake Kirsch
# Module: Game Pieces

# The purpose of this module is to create and define the 
# physical pieces of a board game






import string
import random

class gameRules(object):
	"""
	An object that represents the rule book of scrabble. 
	Used to store information that could potentially 
	change the way the game is played.
	"""

	DEFAULT_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
	}

	DEFAULT_LETTER_DIST = {
	'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
	}

	def __init__(self, let_vals = None, let_dist = None):
		# nothing here yet
		self.letter_values = let_vals if let_vals is not None else gameRules.DEFAULT_LETTER_VALUES
		self.letter_dist = let_dist if let_dist is not None else gameRules.DEFAULT_LETTER_DIST

	def retrieve_value(self, character):
		'''Return value of a letter as int'''
		assert type(character) == str
		return int(self.letter_values[character])

	def get_letter_values(self):
		'''Return letter values dict'''
		return self.letter_values

	def get_letter_dist(self):
		'''Return letter values dict'''
		return self.letter_dist

	


	# def setLetterValues(self, dictionary):
	# 	'''update letter values dict'''
	# 	assert type(dictionary) == dict
	# 	self.letter_values = dict
	
	def __str__(self):
		'''Print letter_values dictionary'''
		return str(self.letter_values)

class letter(object):
	"""
	An object that represents a physical letter.
	Assumes character is a string of length one of 
	ascii.lowercase and value is taken from game rules
	"""
	def __init__(self, game_rules, character):
		'''Create a letter'''
		assert type(character) == str
		assert type(game_rules) == gameRules

		self.character = string.lower(character)
		self.value = game_rules.retrieve_value(character)

	def getValue(self):
		'''Returns point value of the letter'''
		return self.value

	def getCharacter(self):
		'''Return the character of the letter'''
		return self.character

	def __lt__(self, letter):
		'''Returns True if value of self is less than value of 
		letter'''
		return self.getValue() < letter.getValue()
	
	def __le__(self, letter):
		'''Returns True if value of self is less than or equal
		 to value of letter'''
		return self.getValue() <= letter.getValue()

	def __gt__(self, letter):
		'''Returns True if value of self is greater than
		value of letter'''
		return self.getValue() > letter.getValue()
		
	def __ge__(self, letter):
		'''Returns True if value of self is greater than or 
		equal to value of letter'''
		return self.getValue() >= letter.getValue()

	def __eq__(self, letter):
		'''Returns True if value of self is equal to value of letter'''
		return self.getValue() == letter.getValue()
	
	def __str__(self):
		'''Returns character'''
		return self.character

class bag(object):
	'''
	An object that represents the bag of letters, which is a 
	dictionary of 
	'''
	def __init__(self, game_rules):
		self.letters = {}
		# self.letters = self.update_state(game_rules.get_letter_dist())

	def number_of_letters(self):
		'''Return number of letters in bag, number is int'''
		count = 0
		for key, value in self.letter_dict:
			count += value

		return int(count)

	def add_letters(self, addition_dict):
		'''Simulates when a letter puts back letters
		Assumes addition_dict is a dictionary with single
		char, int pairs
		'''
		assert type(addition_dict) == dict
		
		for key, value in addition_dict:
			self.letters[key] = self.letters.get(key,0) + value 

	def valid_removal(self, removal_dict):
		'''Determines if the removal dict is a valid play
		Assumes removal is a dict with single char, int pairs
		Returns True if all letter/int pairs are available in 
		bag
		'''
		assert type(removal_dict) == dict

		#IMPROVE_LATER
		result = []
		for key, value in removal_dict:
			if self.letters.get(key,0) > removal_dict.get(key):
				result.append(True)
			else:
				result.append(False)
		return all(result)


	def remove_letters(self, removal_dict):
		'''Update state of bag based on removal
		Assumes letter_dict is a dictionary of letters
		'''
		if self.valid_removal(removal_dict):
			for key, value in removal_dict:
				self.letters[key] -=  value
			print("Letters removed")
		else:
			print("Invalid removal")


	# def give_letters(self, n):
	# 	'''Simulates when a player asks for n letters
	# 	Assumes n is int. Will update state of bag after
	# 	'''
	# 	# random.randint()
		


# Main Program - some testing right now
if __name__ == '__main__':
	print("test")