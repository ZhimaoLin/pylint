def f1():
    print("this is f1")
    return 5
def f2():
    print("this is f2")
def f3():
    print("this is f3")
    f1()
    f2()
def main():
    a = 3
    b = 4
    a = b
    a = f1()
    a += f2()
    a, b = f1()
    f3()

    if a > 2:
        print()
    elif True:
        print()
    else:
        f3()
    
    for i in range(1, 10):
        print(i)
        while a > 2:
            # a -= 1
            f1()

    try:
        print()
    except:
        f3()
    finally:
        print()
