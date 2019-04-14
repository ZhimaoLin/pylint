# 7.1 Methods have more than 5 arguments
def main():
    a_sun = Sun()

class Sun():
    def __init__(self): 
        pass

    def six_arg_func(self, one, two, three, four, five, six):
        print(one, two, three, four, five, six, "too many args :(")

main()
