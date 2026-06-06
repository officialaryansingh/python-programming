# Q5.> Write a program which finds out whether the enter name is present
# in a list or not.
# Solution.> 

name_list = ["Aryan","Harry","KD","Mishra","Bad Man","Bat Man","Asnish Sonar"]
name_list_lower = list(map(lambda x : x.lower(),name_list))

n = input("Enter your name : ")
if(n.lower() in name_list_lower):
    print("yes your name is the in list")
else:
    print("No your name is not there in the list.")
print("\n\n\nEnd of program\n")

print(name_list_lower)