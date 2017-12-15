
from function_parser.FunctionParser import *

ex = 'sin(5*x)'

parser = FunctionParser(ex,twoVar=True)

f = parser.getFunction()




