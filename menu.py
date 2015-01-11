class Menu:
    def __init__(self, description):
        self.options = []
        self.name = "Menu"
        self.options = []
        self.lastchoice = -1
        self.name = description

    def addoption(self, description, f):
        assert(isinstance(description, str))
        assert(len(self.options) < 9)
        self.options.append([description, f])

    def start(self):
        while True:
            print "-" * len(self.name)
            print self.name
            print "-" * len(self.name)

            i = 1
            for o in self.options:
                print "[%d] - %s" % (i, o[0])
                i += 1

            print
            print "[0] - Back"

            c = raw_input("Choice [%d]: " % (self.lastchoice+1))

            if len(c) == 0:
                ci = self.lastchoice
            else:
                ci = int(c)-1

            if ci == -1:
                self.lastchoise = -1
                return

            if ci < 0 or ci >= len(self.options):
                continue

            self.lastchoice = ci

            self.options[ci][1]()
