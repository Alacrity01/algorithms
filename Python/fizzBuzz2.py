import numpy as np
import timeit


def fizzBuzzClassic():  # Write a function that prints.... from 1 to 100 (inclusive)
    for i in range(1, 101):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


def fizzBuzzAlt(n):  # Write it a completely different way, regardless of efficiency
    for i in range(1, n + 1):
        s = ""  # "Assemble the string approach": really inefficient, but sufficiently odd
        if i % 3 == 0:
            s += "Fizz"
        if i % 5 == 0:
            s += "Buzz"
        if s == "":
            s = str(i)
        print(s)
    return


# Check a single number n using FizzBuzz rules, add to dictionary, and print
def fizzLookup(n, fizzDict={}):
    try:
        print(fizzDict[n])
    except:
        if n % 5 == 0 and n % 3 == 0:
            fizzDict[n] = "FizzBuzz"
        elif n % 3 == 0:
            fizzDict[n] = "Fizz"
        elif n % 5 == 0:
            fizzDict[n] = "Buzz"
        else:
            fizzDict[n] = str(n)
        print(fizzDict[n])
    finally:
        return fizzDict


# Use a helper method to populate or add to a FizzBuzz dictionary from 1 to n
def fizzHash(n, fizzDict={}):
    for i in range(1, n + 1):
        fizzDict = fizzLookup(i)
    return fizzDict


def printFizzDict(fizzDict):
    [print(f"{k}: '{v}'") for k, v in fizzDict.items()]


def saveDict(fizzDict, filename='numpyDict.npy'):
    np.save(filename, fizzDict)  # Save using numpy


def loadDict(filename='numpyDict.npy'):
    savedDict = np.load(filename, allow_pickle='TRUE').item()
    return savedDict


fizzDict = loadDict('fizzDict.npy')
# fizzDict = fizzLookup(1031, fizzDict)
saveDict(fizzDict, 'fizzDict.npy')
printFizzDict(loadDict('fizzDict.npy'))

# fizzDict = fizzHash(100)
# printFizzDict(fizzDict)

# fizzBuzzClassic()
# fizzBuzzAlt(100)

# fizzDict = fizzLookup(97)
# fizzDict = fizzLookup(1)
# fizzDict = fizzLookup(3)
# fizzDict = fizzLookup(5)
# fizzDict = fizzLookup(85)
# fizzDict = fizzLookup(15)


# fizzDict = {}
# fizzDict = fizzLookup(100)
# fizzDict = fizzLookup(1000)
# fizzDict = fizzLookup(1000)


# print(fizzDict)
