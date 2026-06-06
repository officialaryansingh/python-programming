# $$$[important for interview]$$$ @tricky
# Q4.> What will the lenght of the following s:
# s = set()
# and lenght after the following steps:
# s.add(20)
# s.add(20.0)
# s.add("20") ?
 
# Solution.>
s = set()
print(len(s)) # set is empty so lenght = 0


s.add(20)
s.add(20.00)
s.add("20")


print(len(s))
# note: as 
print(20 == 20.00) # is true 
# therefore, set have only 2 unique element , and lenght will be 2 but not 3
print(s)