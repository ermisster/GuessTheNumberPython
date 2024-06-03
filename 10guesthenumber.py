import random
pc=random.randint(0,100)
guess=150
a=0
while guess !=pc:
    guess=int(input("type a number?"))
    a=a+1
    if guess<pc:
        print("higher")
    elif guess>pc:
        print("lower")
    else:
        print("correct")



print("you have tried:",a,("times"))
if a < 5:
    print("excellent!")
elif a < 10:
    print("good!")
elif a == pc:
    print("bad!")









