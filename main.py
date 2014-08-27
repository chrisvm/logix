import tree
import evaluate
import pprint
import sys
from parser import Parser
#TODO: Fix EOF error
#TODO: add readline support


def main():
	parser = Parser()

	while True:
		expr = input("> ")
		if expr.lower() in {'quit', 'q'}:
			sys.exit()
		ast = tree.create(parser.parse(expr))

		d = evaluate.find_vars(ast)
		variables = ''
		for v in d:
			variables += v

		print('vars: %s' % str(variables))
		results = evaluate.eval(ast, variables)
		pprint.pprint(results)

	sys.exit()

if __name__ == '__main__':
	main()