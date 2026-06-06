# Q6.> Write a program to calculate the grade of a student
# from his marks from the following scheme:
# 90-100 => Ex
# 80-90 => A
# 70-80 => B
# 60-70 => c
# 50-60 => D
#  <50  => F 
# Solution.>

marks = float(input("Enter your marks : "))

if(90 < marks):
    print(f"{marks} => Ex")

elif(marks > 100 ):
    print("marks entered is invalid")  

elif(marks>80):
    print(f"{marks} => A")

elif(marks>70):
    print(f"{marks} => B")

elif(marks>60):
    print(f"{marks} => C")

elif(marks>50):
    print(f"{marks} => D")

elif(marks<50):
    print(f"{marks} => F")


