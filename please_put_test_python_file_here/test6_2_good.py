# 6.2 Functions have no more than 12 statements
def main():
    few_arg_func()

def few_arg_func():
    apple = 1
    orange = 2
    banana = 3
    banana = apple + orange
    print(banana)
    apple = banana - orange
    print(apple)
    orange = banana - apple
    print(orange)

main()
