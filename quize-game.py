p=0

print("welcome to quize game!")
print("You will get 1 point for 1 question ")

q1= input("who is the richest person of the world?  ")

if q1 == "elon musk":
    print("correct")
    p= p + 1
else:
    print("wrong answer ")

q2 = input("who is the prime minister of bangladesh? ")
 
if q2 == "sheikh hasina":
    print("correct answer")
    p= p+1
else:
    print("incorrect answer")
q3=input("how many countries are there in the world? ")
if q3== "190":
    print("correct damn!!!")
    p=p+1
else:
    print("incorrect answer")


print("Thanks for playing quize game:) your score is",p ,"out of 3") 
