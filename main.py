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
		if expr.lower() in set(['quit', 'q']):
			sys.exit()
		ast = tree.create(parser.parse(expr))

		d = evaluate.find_vars(ast)
		vars = ''
		for v in d:
			vars += v

		print('vars: %s' % str(vars))
		results = evaluate.eval(ast, vars)
		pprint.pprint(results)

	sys.exit()

if __name__ == '__main__':
	main()