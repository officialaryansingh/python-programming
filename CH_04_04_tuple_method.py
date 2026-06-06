a = (1,2,"Aryan","No One",1.25,False,2,1)
print(type(a))
print(a)


no = a.count(1) # a.count() tells how many times element occurs in the tuple
print(no)


print(a.index(2)) # this will only tell us the first occurence of "2" in a
print(a.index("Aryan"))

# other miscellaneous operation(but not method) chatGPT

# 1.Indexing (accessing element):
t = (10,20,30)
print(t[1]) # output '20'

# 2.slicing
t = (1,2,3,4,5)
print(t[1:4]) # output (2,3,4)

#3.length of tuple:
print(len(t)) # output: 5

#4.Membership Test:
# this operation tells wheather the mentioned element
# is the member of tuple or not
print(3 in t) # output: True

  
# 5. Iteration
for item in t:
  print(item)  # this method will print all the element of the list in
               # in vertical order
               # there more uses of this to know
               # for more about 'Iteration' , take help from ChatGPT
# Iteration is possible in :
# Lists: [1,2,3]
# Tuples: (1,2,3)
# Strings: "abc"
#Dictionaries:{"A", "a",1,2,"b"}
#Sets: {1,2,3}

  
  
  # by using double space here 
  # we can print along the iteration opration
  print("happy new year")

for item in t:
 print(item,"yo!")




# 6.Concateration:
# combine tuples usening '+' operators
t1 = (1,2)
t2 = (3,4)
t3 = t1 + t2
print(t3)


# 7.Tuple Unpacking:breaks a tuple into variable
a,b,c = (9,8,7)
print(a,b,c)
#output: 9 8 7



# 8.Repetition: repeat the tuple multiple times
t = (1,2)
print(t*3) # output: (1,2,1,2,1,2)






# 5. Iteration
for item in t:
  print(item)  # this method will print all the element of the list in
               # in vertical order
               # there more uses of this to know
               # for more about 'Iteration' , take help from ChatGPT
# Iteration is possible in :
# Lists: [1,2,3]
# Tuples: (1,2,3)
# Strings: "abc"
#Dictionaries:{"A", "a",1,2,"b"}
#Sets: {1,2,3}


# # 6.Concateration:
# # combine tuples usening '+' operators
#   t1 = (1,2)
#   t2 = (3,4)
#   t3 = t1 + t2
#   print(t3)


#   print("happy new year")
# by using double space here we can print along the iteration opration