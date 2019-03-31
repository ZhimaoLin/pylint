#7.4 Does each user-defined function have 12 or fewer statements?
def many_arg_func():
    apple = 1
    orange = 2
    banana = 3
    banana = apple + orange
    print(banana)
    apple = banana - orange
    print(apple)
    orange = banana - apple
    print(orange)
    banana = apple + orange
    print(banana)
    apple = banana - orange
    print(apple)
    orange = banana - apple
    print(orange)
