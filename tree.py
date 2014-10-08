__author__ = 'christianvelez'
from nodes import *

def create(l):
	if type(l) == list:

		if len(l) <= 2:
			if l[0] == '-':
				#print('created_negexpr')
				return NegExpr(create(l[1]))
			else:
				return create(l[0])

		if l[1] == '->':
			#print('created_thenexpr')
			return ThenExpr(create(l[0]), create(l[2:]))
		if l[1] == 'V' or l[1] == 'v':
			#print('created_orexpr')
			return OrExpr(create(l[0]), create(l[2:]), exclusive=False)
		if  l[1] == 'X' or l[1] == 'x':
			return OrExpr(create(l[0]), create(l[2:]), exclusive=True)
		if l[1] == '^':
			#print('created_ifexpr')
			return AndExpr(create(l[0]), create(l[2:]))

	elif type(l) == str:
		#print('created_var')
		return Variable(l.lower())

if __name__ == '__main__':
	parsed = [['-', [['p', '->', 'q'], 'V', ['P', '->', 'S']]], '->', [['-', 'P'], '^', 'R', '^', 'S']]
	print(create(parsed))