# 1. sum of n numbers

n = int(input())
a = 0
for i in range(n):
    b = int(input())
    a += b
print (a)

# 2. number of different objects in list

ans = 0
s = set()
for obj in objects: # доступная переменная objects
    if id(obj) not in s:
        s.add(id(obj))
        ans+=1
print(ans)

# 3. returns y >= x and y % 5 == 0

def closest_mod_5(x):
    if x % 5 == 0:
        return x
    y = x+1
    while y % 5 != 0:
        y += 1
    return y

# 4. the number of combinations in n size k

n,k = map(int, input().split())
def C(n,k):
    if k == 0:
        return 1
    if k > n:
        return 0
    return C(n-1,k) + C(n-1,k-1)
print (C(n,k))

# 5. namespace emulator

all_spaces = [{'name':'global','parent':None, 'items':[]}]
 
def create(ns,parent):
	all_spaces.append({'name':ns,'parent':parent, 'items':[]})

def add(ns,var):
	for i in all_spaces:
		if i['name'] == ns:
			i['items'].append(var)
			break

def get(ns,var):
	for i in all_spaces:
		if i['name'] == ns:
			if param in i['items']:
				return (i['name'])
			else:
				return get(i['parent'],var)

n = int(input())
for i in range(n):
	func, ns, param = input().split()
	if func == "create":
		create(ns,param)
	elif func == "add":
		add(ns,param)
	elif func == "get":
		print(get(ns,param))

# 6. money box class

class MoneyBox:
	def __init__ (self, capacity):
		self.capacity = capacity
		self.v = 0
	def can_add (self, v):
		if (self.capacity - self.v) < v:
			return False
		else:
			return True
	def add (self, v):
		self.v += v
		return self.v

# 7. buffer class

class Buffer:
	def __init__ (self):
		self.v = []
	def add (self, *a):
		self.v += list(a)
		while len(self.v) // 5 != 0:
			print(sum(self.v[:5]))
			self.v = self.v[5:]
	def get_current_part (self):
		return self.v

# 8. inheritance determinant

def isAncestor (A, B, d = d):
    if A not in d or B not in d:
        return 'No'
    elif A == B:
        return 'Yes'
    elif d[B] == []:
        return 'No'
    elif A in d[B]:
        return 'Yes'
    else:
        for i in d[B]:
            if isAncestor(A, i) == 'Yes':
                return 'Yes'
        return 'No'
d = {}
nLines = int(input())
for i in range(nLines):
    lisT = input().split(' : ')
    if len(lisT) == 1:
        d[lisT[0]] = []
    else:
        d[lisT[0]] = lisT[1].split()
nLines = int(input())
for i in range(nLines):
    lisT = input().split()
    print (isAncestor(lisT[0], lisT[1]))

# 9. extended stack class

class ExtendedStack(list):
    def sum(self):
        self.append(self.pop() + self.pop())
    def sub(self):
        self.append(self.pop() - self.pop())
    def mul(self):
        self.append(self.pop() * self.pop())
    def div(self):
        self.append(self.pop() // self.pop())

# 10. list with log

import time

class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))     

class LoggableList(list, Loggable):
    def append (self, a):
        list.append(self, a)
        self.log(a)