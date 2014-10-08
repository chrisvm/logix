import tree
import evaluate
import pprint
import sys
from parser import Parser


def main():
	parser = Parser()
	while True:
		# Get input 
		expr = input("> ")
		
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