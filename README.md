logix
=====

Logix is a python module for parsing logic propositions, of the kind "p -> q", "p ^ q -> (q->p)", etc. 
It parses and then evaluates, allowing for infinite recursion of parenthesis and prepositions. It is written for Python 3 and
uses the pyparsing package. 

***Things to do***

  - add readline support (errors in the command line are permanent)
  - pretty printing the dict with the eval of a statement 
  - error when ctrl-d'ing out of the program 
