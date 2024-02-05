class Fib:
    def __init__(self, nn):
        print("__init__")
        self.__n = nn
        self.__i = 0
        self.__p1 = self.__p2 = 1
    def __iter__(self):
        print("__iter__")
        return self
    def __next__(self):
        print("__next__")
        self.__i += 1
        if self.__i > self.__n:
            raise StopIteration
        if self.__i in [1,2]:
            return 1
        ret = self.__p1 + self.__p2
        self.__p1,self.__p2 = self.__p2, ret
        return ret
for i in Fib(10):
    print(i)
    def fun(n):
        for i in range(n):
            yield i
for v in fun(5):
    print(v)
def power(n):
    pow = 1
    for i in range(n):
        yield  pow
        pow *= 2
    for v in power(8):
        print(v)
def Fib(n):
 p = pp = 1
 for i in range(n):
    if i in [0, 1]:
        yield 1
 else:
    n = p + pp
    pp, p = p, n
    yield n
fibs = list(Fib(10))
print(fibs)
two = lambda : 2
sqr = lambda x : x * x
pwr = lambda x, y : x ** y

for a in range(-2, 3):
    print(sqr(a), end=" ")

    print(pwr(a, two()))
def outer(par,loc):
    loc = par
    def inner ():
        return loc
    return inner()
var = 1
fun = outer(var)

print(var)
print()

