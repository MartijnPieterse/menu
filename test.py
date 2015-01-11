from menu import *

def f(s):
    print s

m = Menu("Startmenu")
m.addoption("start", lambda:f("start"))
m.addoption("stop", lambda:f("stop"))
m.addoption("go", lambda:f("go"))
m.addoption("with", lambda:f("with"))

m2 = Menu("Submenu")
m2.addoption("alleen deze", lambda:f("x"))

m.addoption("submenu", m2.start)

m.start()
