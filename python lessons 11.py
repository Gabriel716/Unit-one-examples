
##while True:
##   familar_name=input("common name friends/family use")
##    if familar_name.isalpha():
##        break
##    else:
##        print("Please use a word without spaces", familar_name + "\n")



##S=input("How many small shirts")
##M=input("How many medium shirts")
##L=input("How many large shirts")
##def size(S,M,L):
##    while True:+
##        S=input("How many small shirts")
##        M=input("How many medium shirts")
##        L=input("How many large shirts")
##        end=input('enter "exit" when you are finished')
##        if end=="exit":
##            print("You are finished")
##            break
##    
##size(S,M,L)

num_1 = ""
num_temp = ""
num_final = ""
while True:
    num_1 = input("Enter an integer: ")
    if num_1.isdigit():
        num_final = num_temp + num_1
        num_temp = num_final
    else:
        print(num_final)
        break
