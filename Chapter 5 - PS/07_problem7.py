# Q7.>If the name of the two friends are same.
# What will happen to program in problem 6?
# sollution.> 


d = {"Aryan" : input("enter your fevorite language Aryan :",),
     "ADKD" : input("enter your fevorite language ADKD :",),
     "Mishra" : input("enter your fevorite language mishra :",),
     "Mishra" : input("enter your fevorite language Mishra :",)
     }
# now we have 2 mishras in our dict. 
print(d.items()) 
print(d)

# dict. will consider only the last occurence of same value
