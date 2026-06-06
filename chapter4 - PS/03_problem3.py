# Q.>Check that a tuple cannot be chaged in python .
# soln.
# ATQ, we have to show that doing operation on will not change the tuple either
# it will lead to the formation of new tuple i.e. tuple are imutable

a = (3,4,"no one")

a[1] = 45 
# TypeError: 'tuple' object does not support item assignment