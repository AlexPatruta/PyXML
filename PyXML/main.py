from PyXML import *

xml = PyXML("test.xml")

if __name__ == "__main__":
    print("Main thread execution:\n")
    print(xml.GetLog())
