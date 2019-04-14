# 5.2 Literal assignment statements in a function are within 5 lines of the function name
def main():
    print("this is main!")
    print("this is test")
    print1000()

def print1000():
    apple = 10
    orange = 20
    banana = 30
    return apple, orange, banana

main()
