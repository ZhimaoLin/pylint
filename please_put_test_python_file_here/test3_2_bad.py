# 3.2 Other names do not follow the snake-case style
import random
ONE = 1
TWO = 2
def main():
    foo_test()

def foo_test():
    orange_apple = random.randint(1, 3)
    if orange_apple < 3:
        orange_apple += 1
    if ONE:
        apple_Orange = TWO - ONE
        appleOrange = TWO + ONE
    return apple_Orange, appleOrange

main()
