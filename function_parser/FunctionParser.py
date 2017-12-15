from lexical_analyzer.FunctionLexer import *
from lexical_analyzer.lexer_exceptions.NoSuchSymbolException import *
from function_parser.parser_exceptions.InvalidInputException import *
from function_parser.functions import *



class FunctionParser():
    '''
    Clase para parseo de strings que contienen funciones.
    El objetivo de esta clase es crear una funcion lambda
    en base a un string.
    '''

    def __init__(self, inputString, twoVar=False):
        '''
        Constructor.
        Define el atributo 'inputString' para almacenar la funcion entrante.
        :param inputString: string que contiene la expresion de la funcion.
        '''
        self.__inputString = inputString
        self.__twoVariables = twoVar
        self.__f = self.__convertToFunction(inputString)

    def __convertToFunction(self, inputString):
        '''
        Metodo privado que realiza la conversion del string.

        :param inputString: string de la funcion.
        :return: la funcion que define el string.
        :raise InvalidInputException: si el string de entrada no es una expresion matematica.
        :raise SyntaxError: si el string de entrada no esta bien escrito.
        '''

        # Se valida que sea una expresion matematica.
        try:
            if self.__twoVariables:
                l = FunctionLexer(inputString, 'x', 'y')
            else:
                l = FunctionLexer(inputString)

            l.tokenize()
        except NoSuchSymbolException:
            raise InvalidInputException("Lo ingresado no es una funcion matematica.")

        # Se realiza la ccnversion.
        # Se utiliza eval(), quien es que tirara la excepcion si no esta bien escrita.

        try:

            if self.__twoVariables:
                return lambda x, y: eval(inputString)
            else:
                return lambda x: eval(inputString)
        except Exception:
            raise SyntaxError("La funcion no esta bien escrita.")

    def getFunction(self):
        return self.__f
