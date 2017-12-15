
from function_parser.FunctionParser import *

ex = 'sin(0.2.*x)'

parser = FunctionParser(ex)

f = parser.getFunction()

print(f(2))



