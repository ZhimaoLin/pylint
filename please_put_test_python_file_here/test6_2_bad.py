# 6.2 Functions have more than 12 statements
def main():
    many_arg_func()

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

main()
