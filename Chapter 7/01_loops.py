# some time we need a set of data in a certain order and in a large amount,
# ex. we want to print no. 1 - 100
# we do it with traditional method with lots of efforts 
# but we need to be quick and efficint 
# therefore, we use "loops" in python
# loops are of mainly two type:
# 1.>while  2.>for


# 1. while loop:
# syntax:
#        while(condition):           =>the block keeps executing 
#             #body of the loop        until the condition is true

# -in while loop the condition is checked first.If it evaluates to true,
# the Body of the loop is executed , otherwise not!
# -If the loop is entered , the process of [condtion check & execution]
# is continued until the condition becomes false.


# Quick Quiz: Write a program to print 1-50 using a while loop.
# solution.>

i = 1  # write i = 1 so that it's execution for the give cond.n is first i's true value
while(i<51):
    print(i) # if run this program will run till infinite loop and will print 1 only
    i += 1 # we know "+=" will increse the value of i=1 by 1 since ,
           # and there is a indentation(the double space automatically after using while(),for(),if(,else(),elif()))
           # which shows that we have intered into the while loop,and this will be executed 
           #till the condition do not become false i.e. i == 51 , after every print(i)
           #the value of i changes and since it is in while loop it will be again executed
           #unless the value of i becomes equal to 51, for i = 51 program will not be executed
           