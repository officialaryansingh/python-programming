# Q3.> A spam is defined as a text conditioning following key words:
# "Make a lot of money","buy now","subscribe this","click here","click this",
# "need money ,help!"
# solution.>
a,b,c,d,e,f = ("Make a lot of money","buy now","subscribe this","click here","click this",
     "need money ,help!")

m = input("Enter the message : ")

if(m.count(a)>0 or m.count(b)>0 or m.count(c)>0 or m.count(d)>0 or m.count(e)>0 or m.count(f)>0):
    print("This is a spam message")
else:
    print("normal message")   




# another method , by Harry: introducing new function "in"
# this fuction is just like count funtion but it tells whether the datatype 
# is the part of the other datatype or not
# it's result is True,False
ar = "hello we introduce you a new comand \"in\""
print("introducing" in ar ) # result is false
print("we you" in ar) # output : False
print(("we" in ar))  # output: True
print("we", "you" in ar) # output: we True
# print(("we", "you") in ar): this wrong method




# using "in" function in Q3 
a,b,c,d,e,f = ("Make a lot of money","buy now","subscribe this","click here","click this",
     "need money ,help!")

if((a in m) or (b in m) or (c in m) or (d in m) or (e in m) or (f in m) ):
    print("This comment is a spam!")
else:
    print("This message is not a spam.(^-_-^)")


