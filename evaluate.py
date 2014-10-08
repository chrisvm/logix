__author__ = 'christianvelez'
from itertools import product


class HashDict(dict):
	"""
	hashable dict implementation, suitable for use as a key into
	other dicts.

		>>> h1 = HashDict({"apples": 1, "bananas":2})
		>>> h2 = HashDict({"bananas": 3, "mangoes": 5})
		>>> h1+h2
		HashDict(apples=1, bananas=3, mangoes=5)
		>>> d1 = {}
		>>> d1[h1] = "salad"
		>>> d1[h1]
		'salad'
		>>> d1[h2]
		Traceback (most recent call last):
		...
		KeyError: HashDict(bananas=3, mangoes=5)

	based on answers from
	   http://stackoverflow.com/questions/1151658/python-hashable-dicts

	"""
	def __key(self):
		return tuple(sorted(self.items()))
	def __repr__(self):
		return "{0}({1})".format(self.__class__.__name__,
								 ", ".join("{0}={1}".format(
									 str(i[0]),repr(i[1])) for i in self.__key()))

	def __hash__(self):
		return hash(self.__key())
	def __setitem__(self, key, value):
		raise TypeError("{0} does not support item assignment"
						.format(self.__class__.__name__))
	def __delitem__(self, key):
		raise TypeError("{0} does not support item assignment"
						.format(self.__class__.__name__))
	def clear(self):
		raise TypeError("{0} does not support item assignment"
						.format(self.__class__.__name__))
	def pop(self, *args, **kwargs):
		raise TypeError("{0} does not support item assignment"
						.format(self.__class__.__name__))
	def popitem(self, *args, **kwargs):
		raise TypeError("{0} does not support item assignment"
						.format(self.__class__.__name__))
	def setdefault(self, *args, **kwargs):
		raise TypeError("{0} does not support item assignment"
						.format(self.__class__.__name__))
	def update(self, *args, **kwargs):
		raise TypeError("{0} does not support item assignment"
						.format(self.__class__.__name__))
	def __add__(self, right):
		result = HashDict(self)
		dict.update(result, right)
		return result

def permutations_for_variables(vars):
	prod = list(product([True, False], repeat=len(vars)))
	return [ { vars[x]: v[x] for x in range(len(vars)) } for v in prod ]

def reval(ast, var):
	if ast.name == 'NegExpr':
		return not reval(ast.expr, var)

	if ast.name == 'ThenExpr':
		return (not reval(ast.lexpr, var)) | reval(ast.rexpr, var)

	if ast.name == 'OrExpr':
		if ast.exclusive:
			a = reval(ast.lexpr, var)
			b = reval(ast.rexpr, var)
			return (a or b) and (not (a and b))
		else:
			return (reval(ast.lexpr, var)) | (reval(ast.rexpr, var))

	if ast.name == 'AndExpr':
		return (reval(ast.lexpr, var)) and (reval(ast.rexpr, var))

	if ast.name == 'Variable':
		return var[ast.string.lower()]

def find_vars(ast, d=set()):
	if ast.name == 'Variable':
		v = ast.string.lower()
		if not v in d:
			d.add(v)
		return d
	else:
		if ast.name in {'AndExpr', 'OrExpr', 'ThenExpr'}:
			find_vars(ast.lexpr, d)
			find_vars(ast.rexpr, d)
			return d
		elif ast.name == 'NegExpr':
			return find_vars(ast.expr, d)

def eval(ast, vars='pq'):
	tt = permutations_for_variables(vars)
	return [{HashDict(k): reval(ast, k)} for k in tt]

if __name__ == '__main__':
	import tree

	parsed = ['p', '->', 'q']
	ast = tree.create(parsed)

	print(ast)
	print(eval(ast, 'pq'))