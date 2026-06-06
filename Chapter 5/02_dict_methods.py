d = {} # This is how we write empty dictionary
#  remember it for next topic sets

marks = {
    "Aryan": 100,
    "Subham":56,
    "Rohan": 23,
    0: "Anish Sonar"
}
print(len(marks))
print(marks.items()) # this returns a list of (key,value tuples)
# output: dict_items([('Aryan', 100), ('Subham', 56), ('Rohan', 23), (0, 'Anish Sonar')])

print(marks.keys()) # this returns a list of dictionary's keys
# output : dict_keys(['Aryan', 'Subham', 'Rohan', 0])

print(marks.values()) 
# the .values() method is used to retrive all the value stored in a python dictionary.
# It returns a view object that displays a dynamic view of the dictionary's value,
# meaning if the dictionary changes, the view updates as well.
# i.e. output  will be key's values :
#  dict_values([100, 56, 23, 'Anish Sonar'])


marks.update({"ADKD": 55}) 
# Updates the dictionary with supplied key-value pairs
# now output of print(marks[ADKD]) will be : 55
# instead of 56 as our dict. key's value of ADKD is updated to 55
# hence, dictionarys are mutable   

print(marks["ADKD"])# here output will be 55

#  we can also append i.e. we can introduce or multipule new dictiories at same time
# i.e.
marks.update({0:"Anish Sonar: Black boy", "Nithin":"batman but: he is fat boy",
              "Anushu Raj marks": 50})
# in above code key '0' got updated but here we also introduced new dictionary
# of keys "Nithin" and "Anshu raj marks" 

print(marks)





print(marks.get("Aryan")) # output : 100
# this function returns the value of the spcified keys
# (and value is returned eg "Aryan" is retuned here )



# $$$$  [VERY IMPORTANT POINT FOR INTERVIEW]   $$$$
# TPOIC: What is the diffecrence between print(marks.get(key of dictonary)) comand and
# print(marks[key of dictonary]) , if both give same result when the mentioned 
# key is actually present in the marks named dictionary
# 
# i.e.

print(marks.get("Nithin")) #output : 'batman but: he is fat boy'
print(marks["Nithin"])   #output : 'batman but: he is fat boy'
# above case Nithin is a existing key of the marks dictonary
# here we see no difference 

# but, in case when mentioned key not exists dictionry , 
# eg. ADKD2 this does not exists in dictionary keys
# so here we see the deference in results

print(marks.get("ADKD2")) # ouput: None

print(marks["ADKD2"])  # ouput : key error


# why does it matter : may be case of big data it is good to use .get()