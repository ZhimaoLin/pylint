#6.1 Does every literal (other than 0, 1, 2, -1, 0.0 and '') appear exactly once?
def print1000():
    print(1000)
def main():
    print("this is main!")
    print1000()
class sun:
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
main()
