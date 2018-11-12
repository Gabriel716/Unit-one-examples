#Gabriel Harrison
#11/8/2018
#Crossword Puzzle
print("Python terms")
#Puzzle format
puzzel="""
fjvfloatdy
yopxednins
mspfycnnal
xeaeeukgei
slufryprlc
abeeiagcoi
buclqttbon
gojlivxobg
admyahgerj
stringwvrs
"""
print(puzzel[0:10])
print(puzzel[10:20])
print(puzzel[20:30])
print(puzzel[30:40])
print(puzzel[40:50])
print(puzzel[50:60])
print(puzzel[60:70])
print(puzzel[70:80])
print(puzzel[80:90])
print(puzzel[90:])
print(puzzel)
print("Word List")
#Word list
word_list="float,while,if,boolean,double,operators,string,slicing,index"
print(word_list)
word1=input("Enter the index positions of float")
word1_length=len("float")
word2_length=len("while")
word3_length=len("if")
word4_length=len("boolean")
word5_length=len("double")
word6_length=len("operators")
word7_length=len("string")
word8_length=len("slicing")
word9_length=len("index")

#Word1 index stuff
i=0
found_word=""
while i<word1_length:
    index=word1[i]
    index=int(index)
    found_word=found_word+puzzel[index+1]
    i+=1
print(found_word)
#Word2
word2=input("Enter the index positions of while")
i=0
found_word=""
while i<word2_length:
    index=word2[i]
    index=int(index)
    found_word=found_word+puzzel[index+1]
    i+=1
print(found_word)
#Word3
word3=input("Enter the index positions of if")
i=0
found_word=""
while i<word3_length:
    index=word3[i]
    index=int(index)
    found_word=found_word+puzzel[index+1]
    i+=1
print(found_word)
#Word4
word4=input("Enter the index positions of boolean")
i=0
found_word=""
while i<word4_length:
    index=word4[i]
    index=int(index)
    found_word=found_word+puzzel[index+1]
    i+=1
print(found_word)
#Word5
word5=input("Enter the index positions of string")
i=0
found_word=""
while i<word5_length:
    index=word5[i]
    index=int(index)
    found_word=found_word+puzzel[index+1]
    i+=1
print(found_word)
#Word6
word6=input("Enter the index positions of operators")
i=0
found_word=""
while i<word6_length:
    index=word6[i]
    index=int(index)
    found_word=found_word+puzzel[index+1]
    i+=1
print(found_word)
#Word7
word7=input("Enter the index positions of while")
i=0
found_word=""
while i<word7_length:
    index=word7[i]
    index=int(index)
    found_word=found_word+puzzel[index+1]
    i+=1
print(found_word)
#Word8
word8=input("Enter the index positions of slicing")
i=0
found_word=""
while i<word8_length:
    index=word8[i]
    index=int(index)
    found_word=found_word+puzzel[index+1]
    i+=1
print(found_word)
#Word9
word9=input("Enter the index positions of index")
i=0
found_word=""
while i<word9_length:
    index=word9[i]
    index=int(index)
    found_word=found_word+puzzel[index+1]
    i+=1
print(found_word)


#Examples of slicing

##name1="colette"
##print(name1[2:5])
##print(name1[:4])
##print(name1[4:])
##print(name1[:])
##print(name1[::2])
##print(name1[1::3])
      
      
