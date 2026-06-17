for i in range(100):
    print(i)
    if(i==10):
        break
# or

for i in range(3,100,3):
    if(i == 30):  # here in this skip format i will once become equal to 30
                  # and the will breaked but, if instead of i == 31
                  #then in this skip value loop i will never be equal to 31 so 
                  #this for will continue.
        break
    print(i)



""" CONTINUE IN LOOPS """
for i in range(15):
    if(i == 10):
       continue
    print("\n")
    print(i)