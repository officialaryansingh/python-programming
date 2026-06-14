# 2.> "for" loops
# what ever work we can do using whike loop we we can do them using for loops too
# syntax:
l = [ 1,2,3,"aryan".capitalize()]
for item in l:
    print(item)
'''
ouput:
1
2
3
Aryan
'''
for i in range(1,41,3):
    print(i)

# in case of strings:
n = "aryan".capitalize()
for item in n:
    print(item)
'''
Output:
A
R
Y
A
N
'''

for i in range(0,len(n)):
    print(i+1,n[i])