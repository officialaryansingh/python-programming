letter = ''' Dear <|name|>,
You are selected !
<|Date|>  '''
             
print(letter.replace("<|name|>", "Aryan").replace("<|Date|>", "27 february 2050"))

