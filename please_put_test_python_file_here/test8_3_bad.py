#8.3 Does each method in the class satisfy the software quality tests for user-defined functions?
class Sun:
    # It may seem counterintuitive that single naming style
    def __init__(self, iname, irad, im):
        self.name = iname
        self.radius = irad
        self.mass = im
    def get_mass(self):
        return self.mass
    def __str__(self):
        return self.name
    def get_name(self):
        return self.name
    def six_arg_func(self, one, two, three, four):
        self.irad = two
        self.im = four
        print("a line")
        print("another line")
        print("third line")
        print("fourth line")
        print(">? line")
        print(">>? line")
        two = one
        one = self.__str__()
        print("more line?")
        print(one, two, three, four, "good")
        print("a lot of lines!")
        return self.name
    