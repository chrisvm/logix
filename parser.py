__author__ = 'christianvelez'
from pyparsing import *

variables = 'PQRS'

class Parser(object):
	def __init__(self):
		self.variables = variables + variables.lower()
		self.exprStack = list()
		self.parsed = list()

		self.parser = self.create_parser()

	def pushStack(self, s, l, t):
		self.exprStack.append(l)

	def pushUMinus(self, s, l, t):
		if t and t[0] == '-':
			self.exprStack.append("neg")

	def create_parser(self):
		"""
		thenop   :: '->'
		negop    :: '-'
		andop    :: '^'
		orop     :: 'V' | 'v'
		variable :: 'P' | 'Q' | 'R' | 'S'
		negatom  :: negop atom
		atom     :: negatom | variable | '(' expr ')'
		factor   :: atom [ thenop factor ]*
		term     :: factor [ andop factor ]*
		expr     :: term [ orop term]*
		"""
		thenop = Literal('->')
		negop  = Literal('-')
		andop  = Literal('^')
		orop   = CaselessLiteral("V")
		variable = Word(self.variables, max=1)
		lpar = Literal('(').suppress()
		rpar = Literal(')').suppress()

		expr = Forward()
		negatom = Forward()

		atom = (variable | (lpar + expr + rpar) | Group(negatom)).setParseAction(self.pushStack).setParseAction(self.pushUMinus)
		negatom << negop + atom

		factor = Forward()
		factor << (atom + ZeroOrMore((thenop + factor).setParseAction(self.pushStack)))('thenop')
		term = (factor + ZeroOrMore((andop + factor).setParseAction(self.pushStack)))('andop')
		expr << (Group(term + ZeroOrMore((orop + term).setParseAction(self.pushStack))))('orop')

		return expr

	def parse(self, s):
		self.parsed = self.parser.parseString(s)
		return self.parsed.asList()

if __name__ == '__main__':
	parser = Parser()
	parsed = parser.parse('-((p->q)v(P->S))->(-P^R^S)')
	print(parsed)