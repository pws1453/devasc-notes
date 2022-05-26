import math

def add1(num):
    return num + 1

def doubleNum(num):
    return num * 2

def squareNum(num):
    return math.pow(num,2)

def squareRoot(num):
    return math.sqrt(num)

def circumference(radius):
    doublepi = doubleNum(math.pi)
    return round(doublepi * radius,2)