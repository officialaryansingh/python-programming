# syntax
i = 1
while(i<6):
    print(i)
    i+=1
'''
Output:
1
2
3
4
5
'''

# Quick Quiz:write a program to print 1-50 using while loop
i = 1
while(i<51):
    print(i)
    i += 1

# ex. 
i = 0
while(i<5):
    print("harry")
    i = i+1  # this is same as i +=1

# Quick Quiz: write a program to print the contents of the list using while loops.

l = ["Aryan","hello",True,1, 1.045,False,"harry".upper()]

i = 0 # i = 0 as we have to indexing here of list
while(i<len(l)):
    print(l[i])
    i += 1 


# while loops in case of for loop:
n = " Aryan".upper()
i = 0 
while(i<len(n)):
    print(n[i])
    i += 1