# class A(object):
#     a = 1
#     def __init__(self):
#         self.a = self.a

# a = A()
# print(a.a)
# A.a = 2
# print(a.a)

def is_near(s:list):
    return all([s[i] > max(s[:i]) for i in range(1,len(s))])