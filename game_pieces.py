# Scrabble 3D
# ------------------------------------------

# Author: Jake Kirsch
# Module: Game Pieces

# The purpose of this module is to create and define the 
# physical pieces of a board game

import string
import random
import numpy
import helper_functions


class gameRules(object):
	"""
	An object that represents the rule book of scrabble. 
	Used to store information that could potentially 
	change the way the game is played.
	"""

	DEFAULT_LETTER_VALUES = {'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10}

	DEFAULT_LETTER_DIST = {'a': 1, 'c': 1, 'b': 1, 'e': 1, 'd': 1, 'g': 1, 'f': 1, 'i': 1, 'h': 1, 'k': 1, 'j': 1, 'm': 1, 'l': 1, 'o': 1, 'n': 1, 'q': 1, 'p': 1, 's': 1, 'r': 1, 'u': 1, 't': 1, 'w': 1, 'v': 1, 'y': 1, 'x': 1, 'z': 1}

	DEFAULT_BOARD_DIMENSION = (10, 10, 1)

	def __init__(self, let_vals = None, let_dist = None, board_dimension = None):
		# nothing here yet
		self.letter_values = let_vals if let_vals is not None else gameRules.DEFAULT_LETTER_VALUES
		self.letter_dist = let_dist if let_dist is not None else gameRules.DEFAULT_LETTER_DIST
		self.board_dimension = board_dimension if board_dimension is not None else gameRules.DEFAULT_BOARD_DIMENSION 
	
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

	def get_board_dimension(self):
		'''Return the dimensions of the board
		Returns:
			board_dimension, a tuple of form (int, int, int)'''
		return self.board_dimension


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
	
	next_letter_id - used to keep track of letters throughout game state
	owner - used to map a player id onto the owner, 
		this can be updated when use puts bag in the bag
	turn_id - used to set a turn id when played for points
	"""
	
	next_letter_id = 0

	def __init__(self, game_rules, character, owner = None, turn_id = None):
		'''Create a letter'''
		assert type(character) == str
		assert len(character) == 1
		assert type(game_rules) == gameRules
		

		self.character = character.lower()
		self.value = game_rules.retrieve_value(character)
		self.id_num = letter.next_letter_id
		letter.next_letter_id += 1
		self.owner = owner
		self.turn_id = turn_id

	def getValue(self):
		'''Returns point value of the letter'''
		return self.value

	def getCharacter(self):
		'''Return the character of the letter'''
		return self.character

	def get_id_num(self):
		'''Return the id_num of the letter'''
		return self.id_num

	def get_owner(self):
		'''Get owner of the letter object'''
		return self.owner

	def get_turn_id(self):
		'''Return the id_num of the letter'''
		return self.turn_id

	def set_owner(self, owner):
		'''Set owner of the letter
		Parameters:
			owner - a player id
		'''
		assert(type(owner) == int)
		self.owner = owner

	def set_turn_id(self, turn_id):
		'''set turn id of the letter
		Parameters:
			turn_id - int identifying the turn
		'''
		assert(type(turn_id) == int)
		self.turn_id = turn_id


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
	dictionary of {char:value}
	char - single value character representing the letter
	value - int, representing the count of those letters in the bag
	'''

	def __init__(self, game_rules):
		self.letter_dict = {}
		# self.letters = self.update_state(game_rules.get_letter_dist())

	def get_letter_dict(self):
		'''Return the dictionary of available letters'''
		return self.letter_dict

	def number_of_letters(self):
		'''Return number of letters in bag, number is int'''
		count = 0
		for key, value in self.get_letter_dict().items():
			count += value

		return int(count)

	def is_empty(self):
		'''Boolean for whether or not the bag has letters available'''
		return (self.number_of_letters() == 0)

	def add_letters(self, addition_dict):
		'''Simulates when a letter puts back letters
		Assumes addition_dict is a dictionary with single
		char, int pairs
		'''
		assert type(addition_dict) == dict
		
		for key, value in addition_dict.items():
			self.get_letter_dict()[key] = self.get_letter_dict().get(key,0) + value 

	def valid_removal(self, removal_dict):
		'''Determines if the removal dict is a valid play
		Assumes removal is a dict with single char, int pairs
		Returns True if all letter/int pairs are available in 
		bag
		'''
		assert type(removal_dict) == dict

		#IMPROVE_LATER
		result = []
		for key, value in removal_dict.items():
			if self.get_letter_dict().get(key,0) >= value:
				result.append(True)
			else:
				result.append(False)
		return all(result)


	def remove_letters(self, removal_dict):
		'''Update state of bag based on removal
		Assumes letter_dict is a dictionary of letters
		'''
		error = bagRemovalError("Invalid Removal")
		
		if self.valid_removal(removal_dict):
			for key, value in removal_dict.items():
				self.get_letter_dict()[key] -=  value
		else:
			raise error


	def give_letters(self, n):
		'''Simulates when a player asks for n letters
		
		Parameters:
			n - assumes n is int
		Return:
			a dictionary of letters, single char, number pairs
		'''
		# this list holds the suggested draw of letters
		letter_draw = []
		
		# turn self.letter_dict into list, easier to use the random integer
		# this way
		letters_in_bag = helper_functions.dict_to_list(self.get_letter_dict())
		
		# generate a suggested draw of letters from bag
		while (n > len(letter_draw) and len(letters_in_bag) > 0):
			# randomly generate a index value
			idx = random.randint(0, len(letters_in_bag)-1)
			letter_draw.append(letters_in_bag.pop(idx))

		letter_draw = helper_functions.list_to_dict(letter_draw)
		self.remove_letters(letter_draw)
		return letter_draw


		# # this is really a 'generate proposed removal'
		# return_list = []
		# letter_dict_copy = self.get_letter_dict().copy()


		# while (n > 0 and self.number_of_letters() > 0):
		# 	idx = random.randint(0, self.number_of_letters())
		# 	return_list.append(letter_list[idx])
		# 	# do some removals


		# 	n -= 1

		# # # convert return_list to return_dict
		# # return_dict = {}
		# # for i in return_list:
		# # 	return_dict[i] = return_dict.get(i,0) + 1

		# return letter_list


class board(object):
	'''
	An object that represents the gameboard. Gameboard holds letters
	Develop in #D but the Z dimension could be 1, i.e. none
	'''
	def __init__(self, game_rules, letter_positions = {}):
		'''Creates a gameboard according to the game_rules
		Parameters:
			game_rules - an object type game_rules which contains data
				that determines how the remainder of the game is played
			letter_positions - a dict of {location_tuple, letter} where
				location_tuple - of form (x,y,z) representing the location on the board
				letter - of type game_pieces.letter, holding the object letter
		'''
		self.dimensions = game_rules.get_board_dimension()		
		self.letter_positions = letter_positions

	def get_dimensions(self):
		'''Returns a tuple of the board game dimensions'''
		return self.dimensions

	def get_board(self):
		'''Returns the board'''
		return(self.board)
	
	def get_letter_positions(self):
		'''Returns the letter_positions dictionary'''
		return(self.letter_positions)


	def is_valid_location(self, location):
		'''Returns true if the tuple is a valid board game location

		Parameters:
			location - a tuple of 3 integers representing (x,y,z) 
				cordinates
		Returns:
			Boolean - indicating if the tuple is a valid slot on the board
			game based on dimensions defined in gameRules'''
	
		assert type(location) == tuple
		assert(len(location) == 3)
		assert all(list(map(lambda x: isinstance(x, int), location))) == True
		assert all([(x <= y and x >= 1) for x, y in zip(location, self.get_dimensions())])
	
		return True

	def is_location_empty(self, location):
		'''Returns True/False if location of the board game is empty
		
		Parameters:
			location - a tuple of 3 integers representing (x, y, z) coordinates

		Returns:
			Booleawn - indicating if the slot is empty on the board game
		'''
		if self.get_letter_positions().get(location, None) is None:
			return True
		else:
			return False

		# if self.is_valid_location(location):
		# 	x = location[0]
		# 	y = location[1]
		# 	z = location[2]
			
		# 	if self.get_board()[z-1][y-1][x-1] == '[ ]':
		# 		return True
		# 	else:
		# 		return False
		# else:
		# 	return False

	def add_letter(self, letter, location):
		'''Add a letter to the game board object

		Parameters
			letter - a game_pieces.letter object
			location - a tuple of 3 integers, representing (x,y,z) 
			coordinates
		Updates
			Game board state
		
		Returns
			None'''
		invalid_location_error = invalidLocationError("Invalid Location")

		assert(str(type(letter)) == '<class \'game_pieces.letter\'>')
		if (self.is_valid_location(location) and self.is_location_empty(location)):
			self.get_letter_positions()[location] = letter
		else:
			raise invalid_location_error

	def pretty_print_board(self):
		'''Converts the letter_position dictionary into an easily 
		readable output for user'''

		x = self.get_dimensions()[0]
		y = self.get_dimensions()[1]
		z = self.get_dimensions()[2]

		board = [[['[ ]' for i in range(x)] 
			for j in range(y)] 
			for k in range(z)]
		
		for key, value in self.get_letter_positions().items():
			# extract indexes and char for readability
			x = key[0]
			y = key[1]
			z = key[2]
			simple_char = value.getCharacter()
			# update the list representation of the board
			# board[z-1][y-1][x-1] = '{}[{}]{}'.format(helper_functions.bcolors.OKGREEN, simple_char, helper_functions.bcolors.ENDC)
			# board[z-1][y-1][x-1] = '[ ' + helper_functions.bcolors.OKGREEN + simple_char + helper_functions.bcolors.ENDC + ' ]'
			board[z-1][y-1][x-1] = '[{}]'.format(simple_char)
		# create a "pretty arrangement" 
		pretty_arrange = str('\n\n'.join(['\n'.join([''.join(['{:8}'.format(item) 
				for item in row]) 
                for row in level]) 
                for level in board]))
		
		return(pretty_arrange)
		

	def __str__(self):
		'''overload print() for practice'''
		return(self.pretty_print_board())


class gamePieceError(Exception):
    """Base class for exceptions in game_piece Module."""
    pass

class bagRemovalError(gamePieceError):
    """Exception raised for errors in removing letters from bag.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message):
        # self.expression = expression
        self.message = message

class invalidLocationError(gamePieceError):
	'''Exception raised for errors when selecting invalid locations

	Attributes:
		message - explanation of the error
	'''
	def __init__(self, message):
		'''Initialize with message'''
		self.message = message

# Main Program - some testing right now
if __name__ == '__main__':
	print("test")