import tree
import evaluate
import pprint
import sys
import atexit
import readline
from os import path
from parser import Parser


def main():
	# create the parser
	parser = Parser()

	# look for the history file
	hist_file = path.join(path.expanduser('~'), '.logix_history')

	# init history file
	try:
		readline.read_history_file(hist_file)
	except FileNotFoundError:
		pass

	# set histort file save at end of execution
	atexit.register(readline.write_history_file, hist_file)

	while True:
		# Get input
		try:
			expr = input("> ")
		except EOFError:
			print('quit')
			sys.exit()

		# If input 'quit' or 'q', exit the program
		if expr.lower() in {'quit', 'q'}:
			sys.exit()

		# Create the ast 
		ast = tree.create(parser.parse(expr))

		# Get the variables used in the expression 
		# and get a printable repr of them 
		expression_vars = evaluate.find_vars(ast)
		variables = ''
		for var in expression_vars:
			variables += var

		# Print the variables used and the results
		# from the truth table 
		print('vars: %s' % str(variables))
		results = evaluate.eval(ast, variables)
		pprint.pprint(results)

	sys.exit()

if __name__ == '__main__':
	main()