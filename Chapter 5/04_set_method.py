s = {1,2,5,9,43,54,"Aryan"}

#1.> type(s)

print("set s :",s,type(s)) # output: {1,2,43,54,"Aryan",9} <class 'set'>

# 2.> s.add(): this introduces b new element in set existing. 

s.add(0000) # this will add '0' as 000 = 0

s.add(1111)
# s.add(22,"yo!") we can't do this ,i.e. adds and element one at b time

print( "set s :",s,type(s))

print(len(s))

b = { 3,4,54,"Aryan",1.2,3,8,9}

print("set b :", b,type(b))

#3.> b.clear(): make any set into null set 
s.clear()

print("set s :", s)

#4.>b.discard(element): remove an element if it is b member,
# not then do nothing .

b.discard(1.2)
print("set b :", b)

# properties of sets:
# 
# 1. sets are unordered => element order does't matter 
# 2. sets are are indexed => cannot access element by index 
# 
# 3.There is no way to change existing items in sets.But,
# we can remove and add items in sets. 
 
# 4. Sets can not contain duplicate values , can,t be indexed as they ar unordered


print(len(b))
print(len(s))

#  operation on sets :
# consider the following set:
# 
# s = {1,8,4,3} 

# 1.>len(s):returns 4, the length of the set
# 2.>s.remove(8): remove '8'  from s and updates
# 3.>s.pop(): Removes an arbitry(random) element from the set and returns the element removed 
# 4.>s.clear(): Empties the set s i.e. null set
# s.union({8,11}): returns b new set with all item from both sets
# =>{1,8,2,3,11}
# 
# 6.> s.intersection({8,11}):
# returns b set which contains only items that is common in both
# =>output:{8}
# 
# let b = {1,2,3}
# b = { 9,8,3,2}
# print(b.union(b)) : returns- {1,2,3,9,8}


# print(b.intersection(b))  # output: {3,2}
a = {1,2,3,8}
b = {8,11}
print("Line 71",a.update(b))
print(b.union(a))
print(b)

print(b.intersection(a))
print(b)


print(b - b)
print({8,11}.issubset(b))
print("{2,8} is subset of b",{2,8}.issubset(b))
print("{1,2,3,8} is superset of b",{1,2,3,8}.issuperset(b))

print("{3,4,8}is subset of b",{3,4,8}.issubset(b))

print(b.difference(b)) #both line 82 & 83 are same
print(b - b)           #but b-b can be used in other cases too.

print("{8} is superset of b : ",{8}.issuperset(b))
print()

print(b.pop())
print(b)
print(b.pop())
print(b)


