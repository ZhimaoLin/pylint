def f1():
    print("this is f1")
def f2():
    print("this is f2")
def f3():
    print("this is f3")
    f1()
    f2()
def main():
    a = 3

    if a > 2:
        print()
    else:
        f1()
    
    for i in range(1, 10):
        print(i)

    while a > 2:
        print(1)
        a -= 1


    # f3()
