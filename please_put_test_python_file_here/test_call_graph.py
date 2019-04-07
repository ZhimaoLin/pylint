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
    try:
        f1()
        if True:
            if_in_try()
        else:
            else_in_try()
        for i in range(0, 3):
            for_in_try()
    except ZeroDivisionError:
        f2()
        if True:
            if_in_except()
        else:
            else_in_except()
        for i in range(0, 3):
            for_in_except()
    except:
        f2()
        f1()
    finally:
        if True:
            if_in_finally()
        else:
            else_in_finally()
        for i in range(0, 3):
            for_in_finally()
    f3()
    if a < 2:
        f1()
        if True:
            f2()
            while 1:
                function()
        try:
            try_in_if()
            a = f1()
            (a, b) = f1()
            a += f1()
            a, _ = f1()
        except:
            except_in_if()
        finally:
            finally_in_if()
    else:
        f1()
        for i in range(0, 1):
            for_in_else()
        try:
            try_in_else()
        except:
            except_in_else()
        finally:
            finally_in_else()
            while True:
                while_in_finally()

    # f3()
main()