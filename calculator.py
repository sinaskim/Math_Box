#계산기
def add(a,b):
    return a+b

def subtract(a,b):
    return a-b;

def say_hello():
    print("hello");

def multifly(a,b):
    return a*b;

def divide_new(a,b):
    return a/b;

def getMedian(a, b):
    return (a+b)/2;
    
def getRemainder(a, b):
    return a//b;
def devide_premium(a,b):
    return a/b;

def getPercent(a, b):
    return (a/b) * 100;
    return (a+b)/2

def getSum_ver1(n):
    return n(n+1)/2

def factorial(n):
    num = 1
    while n >= 1:
        num = num * n
        n = n - 1
    return num