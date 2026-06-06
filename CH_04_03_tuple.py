# TUPLE: A tuple is a immutable data type.
# i.e. we can not change tuple like in case of list 
# elements of tuple are inside ->'()' 
# while element of a list are stored inside ->[]

a = () # i.e. it is a empty tuple
print(type(a))
print(a)

b = (1) # it is not a tuple datatype
        # it is int. datatype
print(type(b))
print(b)

# in order to creat single value tuple i.e. only with one element
# we use comma ','
a = (1,)
print(type(a))
print(a)
# multi element tuple
a = (1,2,"Aryan","No One",1.25)
print(type(a))
print(a)



