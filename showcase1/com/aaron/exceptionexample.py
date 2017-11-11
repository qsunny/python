# -*- codiing:utf-8 -*-
"""os example"""
__author__="aaron.qiu"

import sys

def valueException():
    while True:
        try:
            x = int(input("Please enter a number: "))
            break
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")

def moreException():
    try:
        print("moreException----")
    except (RuntimeError, TypeError, NameError):
        pass

def readFileContent() :
    try:
        f = open('myfile.txt')
        s = f.readline()
        i = int(s.strip())
    except OSError as err:
        print("OS error: {0}".format(err))
    except ValueError:
        print("Could not convert data to an integer.")
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise


def exceptionElse():
    for arg in sys.argv[1:]:
        try:
            f = open(arg, 'r')
        except IOError:
            print('cannot open', arg)
        else:
            print(arg, 'has', len(f.readlines()), 'lines')
            f.close()


def raiseExceptioin():
    try:
        raise Exception('spam', 'eggs')
    except Exception as inst:
        print(type(inst))  # the exception instance
        print(inst.args)  # arguments stored in .args
        print(inst)  # __str__ allows args to be printed directly,
        # but may be overridden in exception subclasses
        x, y = inst.args  # unpack args
        print('x =', x)
        print('y =', y)
    finally:
        print('Goodbye, world!')

def raiseNameException():
    try:
        raise NameError('HiThere')
    except NameError as ex:
        print('An exception flew by!')
        raise

class MyError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)


def userDefindException():
    try:
        raise MyError(2 * 2)
    except MyError as e:
        print('My exception occurred, value:', e.value)


class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class InputError(Error):
    """Exception raised for errors in the input.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

class TransitionError(Error):
    """Raised when an operation attempts a state transition that's not
    allowed.

    Attributes:
        previous -- state at beginning of transition
        next -- attempted new state
        message -- explanation of why the specific transition is not allowed
    """

    def __init__(self, previous, next, message):
        self.previous = previous
        self.next = next
        self.message = message


if __name__=="__main__":
    #valueException()
    moreException()
    readFileContent()
    exceptionElse()
    raiseExceptioin()
    #raiseNameException()
    userDefindException()