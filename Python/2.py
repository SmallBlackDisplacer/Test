# 1. catch all exceptions:

try: foo() 
except ZeroDivisionError: 
    print("ZeroDivisionError") 
except AssertionError:   
    print("AssertionError")
except ArithmeticError:   
    print("ArithmeticError")

# 2. What exceptions I can remove?

def make_dict (d, stri):
    if len(stri) == 1:
        d[stri[0]] = []
    else:
        d[stri[0]] = stri[1].split()

d = {}
n = int(input())
for i in range(n):
    stri = input().split(' : ')
    make_dict(d, stri)

def isAncestor (winter, OMG):
    if d[OMG] == []:
        return False
    elif winter in d[OMG]:
        return True
    else:
        for i in d[OMG]:
            if isAncestor(winter, i) == True:
                return True
        return False    
    
def isAncestorInList (lis, a):
    for i in lis:
        if isAncestor(i, a):
            return True
    return False

lis = []
n = int(input())
for i in range(n):
    check = input()
    if isAncestorInList(lis, check):
        print (check)
    else:
        lis.append(check)

# 3. PositiveList

class NonPositiveError (Exception):
    pass

class PositiveList (list):
    def append (self, x):
        if x > 0:
            list.append(self, x)
        else:
            raise NonPositiveError

# 4. add days

