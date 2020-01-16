class CsStudent:

    stream = "cse"

    def __init__(self, roll):
      self.roll = roll
    def setaddress(self, address):
       self.address = address
    def getaddress(self, address):
       return self.address

a = CsStudent(101)
a.setaddress("Bukhara, Uzbekistan")
print(a.getaddress(address=True))