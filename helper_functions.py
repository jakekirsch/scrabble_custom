# Scrabble 3D
# ------------------------------------------

# Author: Jake Kirsch
# Module: Helper Functions

# The purpose of this module is to hold some helper functions
# that make other modules more readable


def list_to_dict(letter_list):
	'''
	Helper function to quickly convert a string to a list

	Parameters:
		letter_list - a list of characters in the string
	Returns:
		letter_dict - a dictionary with single value chars as key
						and count of occurences as value
	'''
	assert type(letter_list) == list

	letter_dict = {}

	for i in letter_list:
		assert type(i) == str
		letter_dict[i] = letter_dict.get(i,0) + 1
	return letter_dict

def dict_to_list(letter_dict):
	'''
	Helper function to quickly convert a string to a list

	Parameters:
		letter_dict - a dictionary with single value chars as key
						and count of occurences as value
	Returns:
		letter_list - a dictionary with single value chars as key
						and count of occurences as value
	'''
	assert type(letter_dict) == dict

	letter_list = []
	for key, value in letter_dict.items():
		assert type(key) == str
		assert type(value) == int
		for i in range(0,value):
			letter_list.append(key)
	return letter_list

# helper function to calculate "difference" between tuples.
def tuple_diff(x, y):
    return tuple(map(lambda i,j: abs(i - j), x, y))

def find_edges(graph, start, nodes = []):
	'''Takes a graph, start node and optional list of nodes
	Parameters:
		graph - a dictionary with keys as a tuple representing location 
			of node and a list of tuples representing the nodes that can be reached
		start - a start node from graph
		nodes - a list of the node tuples that can be reached from start tuple
	Output:
		a list of nodes (tuples) that can be reached from the start node'''
	nodes = nodes + [start]
	for node in graph[start]:
		if node not in nodes: 
			nodes = find_edges(graph,node,nodes)
	return nodes    

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'