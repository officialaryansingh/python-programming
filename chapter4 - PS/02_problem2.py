# Q2. Write a program to accept marks of 6 students and display them 
#     in a sorted manner
# soln.> ATQ, i have to write a program where
#       step1 - user will inter the marks of  six students  
#       step2 - input given by the user will be sorted

s1 = float(input("enter the marks of s1 :",))
s2 = float(input("enter the marks of s2 :",))
s3 = float(input("enter the marks of s3 :",))
s4 = float(input("enter the marks of s4 :",))
s5 = float(input("enter the marks of s5 :",))
s6 = float(input("enter the marks of s6 :",))


m = [s1,s2,s3,s4,s5,s6]
# list is defind as element inside sq. brackets '[ ]'
# as we have to write the program that can represents the marks in
# sorted manner so we need to use lists here
# as list are mutable , therfore can be sorted
# but if we use tuple here it will be imutable and we can't sort it 
# and will show error

m.sort()
print(m)
# problem solved ($^_^$)