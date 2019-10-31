def r(n):
    last, rest = n%10, n//10
    if rest == 0:
        return last * 11
    return r(rest) * 100 + last * 11

class A(object):
    a = 1
    
    def __init__(self):
        self.b = 2
        self.__str__ = lambda: 'fuck'

    def __str__(self):
        return 'shit'

class B(A):
    def __init__(self):
        self.c = 3

def in_nested(v, L):
    if type(v) == type(L):
        return v == L
    else:
        return any([in_nested(v,x) for x in L])

class C():
    a = 1

    def __repr__(self):
        return super().__repr__() + 'lol'
    
    # def __str__(self):
    #     return 'shit'