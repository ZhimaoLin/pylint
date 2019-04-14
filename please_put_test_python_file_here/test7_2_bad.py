# 7.2 Methods have more than 12 statements
def main():
    a_sun = Sun()

class Sun():
    def __init__(self):
        pass

    def many_arg_func(self):
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
