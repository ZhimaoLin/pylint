# 3.1 Class names follow the camel-case style
def main():
    pass

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

main()
