import random

def main():
    apple = random.randint(0, 10)

    if apple <= 3:
        print("True branch")
    elif apple > 3 and apple <= 7:
        print("Else if branch")
    else:
        print("False branch")

    
    for i in range(0, 10):
        print("For loop body")

    i = 0 
    while i < 10:
        print("While loop body")


    try:
        print("Try clause")
    except:
        print("Except clause")
    finally:
        print("Finally clause")

    for i in range(0, 10):
        if apple <= 5:
            f1()
        else:
            f2()

def f1():
    print("Function f1 is called.")

def f2():
    print("Function f2 is called.")

main()






