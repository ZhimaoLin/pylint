#8.3 Does each method in the class satisfy the software quality tests for user-defined functions?
def main():
    pass

class Sun:
    # It may seem counterintuitive that single naming style
    def __init__(self, i_m):
        self.name = 'name'
        self.radius = 'radius'
        self.i_rad = 2
        self.i_m = 4
        self.mass = i_m
    def get_mass(self):
        return self.mass
    def __str__(self):
        return self.name
    def get_name(self):
        return self.name
    def five_arg_func(self, one, two, three, four):
        self.i_rad = two
        self.i_m = four
        print("less than 12 lines")
        print(one, two, three, four, "good")
        return self.name

main()
