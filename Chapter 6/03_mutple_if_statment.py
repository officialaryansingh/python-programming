a = int(input("Enter no. :",))
if(a%2 == 0):        # ifs are always independent
    print("no. is even") # If no. is not even then there will not be any outcome
                        #  and we move toward our next code. 

if(a>= 20):
    print("you can do it!")
elif(0<a<20):
    print("keep it up")
elif(a<0):
    print("invalide age")
else:
    print("bye bye")
print("End of program")