class Menu:
    def __init__(self):
        self.options = []
        self.name = "Menu"
        self.options = []

    def setname(self, description):
        self.name = description

    def addoption(self, description, f):
        assert(isinstance(description, str))
        self.options.append(description)

    def start(self):
        print "-" * len(self.name)
        print self.name
        print "-" * len(self.name)

        i = 1
        for o in self.options:
            print " [%d] - %s" % (i, o)
            i += 1

        print
        print " [0] - Back"
