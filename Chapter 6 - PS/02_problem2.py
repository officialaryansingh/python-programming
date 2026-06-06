# Q2> Write a program to find out whether a student has passed or falied in exam
# if it requires a total of 40% and atleast 33% in each subject to pass.
# Assume 3 subjects and take  marks as an input from the user.
# Solution.>
# let a = maths, b= Physics and c = chemistry

a = float(input("Enter your Maths marks :",))
b = float(input("Enter your marks in physics :",))
c = float(input("Enter your chem. marks :")) 
d = 100
if(a*100/d >33):
    print("passed in maths ")
elif(a*100/d <33):
    print("you failed in maths")

if(b*100/d >33):
    print("passed in physics")
elif(b*100/d <33):
    print("you failed in physics")

if(c*100/d >33):
    print("passed in chemistry")
elif(c*100/d <33):
    print("you failed in chemistry")

if(((a+b+c)*100)/(3*d)>40 and (a*100)/d and (b*100)/d and (c*100)/d):
    print("congrats you passed in exams ")
else:
    print("You did't passed, try again.,better luck next time")
