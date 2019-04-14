# 7.1 Methods have no more than 5 arguments
def main():
    a_sun = Sun()

class Sun():
    def __init__(self): 
        pass

    def six_arg_func(self, one, two, three, four):
        print(one, two, three, four)

main()

