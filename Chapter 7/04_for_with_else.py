# we can use for loop with else 
"""IMPORTANT FOR INTERVIEW !!!"""
# this have not much use in real world but interviewer can use it to trap you.

l = [ 1,2,3,"aryan".capitalize()]
for item in l:  # "for" loop will run till it keep om getting values and
                #  then values get exhusted.
    print(item)
else:                  # This is printed when to loop gets exhusted!
    print("\ndone!")