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
    def five_arg_func(self, one, two, three, four):
        self.irad = two
        self.im = four
        print("less than 12 lines")
        print(one, two, three, four, "good")
        return self.name
