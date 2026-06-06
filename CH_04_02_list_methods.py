# in chapter 3 -> string functions leads to new new string but in case of list funtion lists is changed itself, hence there is no new list is formed

enemies = ["appel", "orange", 5, 345.06, False, "Aakash", "Rohan"]

print(enemies)


# ' some list.append()' adds a new element at the end of some list 
enemies.append("Aryan") 

print(enemies)

l1 = [1, 23, 62, 2, 645]

l1[4] = 64
print(l1)
#' l1.sort()' function rearranges the int. elements in the there accendeing order
# this sort function only works only if all the elements of a list is only int. type element 
l1.sort()
print(l1)

# ' l1.reverse()' functons rearranges the int.elements of the list in there decending order
# above function works only if all the elements of the lists are int.type elements

l1.reverse()

print(l1)

# l1.append(8): adds 8 at the end of the list
l1.append("Aryan")
print(l1)

l1.append(4573)
print(l1)
# hence, we do different types of opretion on alist,
# every time our lists get updated or muted to new list,
# repplacing the previous one.

# l1.insert(3,8): This will add 8 at 3 index
l1.insert(3,8)
print(l1)

# l1.pop(5): This will delete the element of list at 5th index and 
# give us the new list with new diffined index
# print(l1.pop(6)) # print(l1.pop(6)) will show which element of the string is poped or deleted
# l1.pop(6) : updated the list to [64,62,23,8,2,1,4573]

print("using pop fuction")
# value = l1.pop() >>> this will remove any of the value rondomly 
value = l1.pop(6) # this will remove the mentioned index of the element at index "6" i.e.Aryan
print(value)
print(l1)

# l1.sort()
# print(l1)

# l1.remove() method used to delete a specific element of the list 
# it's value and not by it's index 
# removes the first occurance of a specified value from the list.
# l1.remove(4573)
# print(l1)

# l1.append(62)
# l1.remove(62)
# print(l1) 