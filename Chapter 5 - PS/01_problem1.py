# Q.1>Write a program to create a dictionary
# of Hindi words with values as their english translation.
# Provide user with an option to look it up!

# solution:
# ATQ, we have to write a program where we create a already well difined dictionary
# and we have to take input from the user as a hindi word within the dictionary  and it will return 
# it's english translation of the hindi word entered by the user.

d = {"tata":"bye bye","tum":"you","vaha":"there","dekho":"see","samundr":"sea"}

n = input("enter the hindi word :",)
print(f"English translation of {n} is : ",d.get(n))

print(f"English translation of\"{n}\" is : ",d[n])



