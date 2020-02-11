from random import *
##function guess
def guess(num,attempt):
    count=0
    for i in range(1,attempt+1):
        print("Enter your",i," attempt")
        x=int(input())
        if x>num:
            count=count+1
            print("Too High")
        elif x<num:
            count=count+1
            print("Too Low")
        elif x==num:
            if count<=attempt:
                print("You Win")
                contnue()
    if count==attempt and x!=num:
        print("You Lost")
        contnue()

#Difference of range
def genNum(start,end):
    try:
        start=int(input("Enter start range"))
        end=int(input("Enter end range"))
        if end-start<50:
            print("Difference between start and end range be >=50.\n")
            genNum(start,end)
        else:
            attempts(start,end)
    except Exception as e:
        print("Only Integers Allowed",e)

#Attempts       
def attempts(start,end):
    attempt=int(input("Enter no. of attempts not more than 10"))
    if attempt<1 or attempt>10:
        attempts(start,end)
    else:
        num=randint(start,end)
        guess(num,attempt)

#Continue Game
def contnue():
    y_no=input("Do you want to play again press:Y/N")
    if y_no=="y" or y_no=="Y":
        genNum(start=0,end=0)
    elif y_no=="n" or y_no=="N":
        exit()
    else:
        contnue()

#Main Program
genNum(start=0,end=0)


