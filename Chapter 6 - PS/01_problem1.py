# Q1.>Write a program to find the greatest of the no. entered by the user.
# solution.>
# since , in set of 4 no.s the the A.M. of three no. will be less than the greatest no.
a = float(input("Enter the no. a :"))
b = float(input("Enter the no. b :"))
c = float(input("Enter the no. c :"))
d = float(input("Enter the no. d :"))

if(a>(d and c and b)):
    print(f"no. a = {a} is greatest")
elif(b>(a and c and d)):
    print(f"no.b = {b} is gratest")
elif(c>(a and b and d)):
    print(f"no. c = {c} is greatest.")
elif(d>(a and b and c)):
    print(f"d = {d} is the greatest no.")
else: 
    print("invalide input")
# NOTE: even if we don't use else  program is copmlete
# all we need in case of condional is "if" if we don't use 
# elif or else then also there will not be any error case . 
print("End of program")
