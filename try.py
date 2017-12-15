
from parser.FunctionParser import *


ex = 'sin(pi*x)'
p = FunctionParser(ex)

f = p.getFunction()

print(f(1/2))
