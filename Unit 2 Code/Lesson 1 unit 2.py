#Gabriel Harrison
#11/6/2018
import random
name="Gabriel Harrison"
length=len(name)
print(length)
index_position=random.randrange(0,length)
char=name[index_position]
print(char)
if index_position<=length:
    char=name[index_position]
else:
    print("That won't work")
