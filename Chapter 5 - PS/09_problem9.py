# Q9.> Can you cange the value inside the list which
# is contained in set s:
# s = {8,7,12,"Aryan",[1,2]}

# Solution.>
# 
# i.> we can't include list in a set
# ii.> we can't change list 
# iii.> we can use set to operate on them and make a new set.
# iv.> we can do opertration on set shown below 
s = {8,7,12,"Aryan",1}
s.discard("Aryan")

print(s)

s2 = {"No One"}

print(s.union(s2))

print(s)