class User:
    def __init__(self, Username, Password):
        self.Username = Username
        self.Password = Password

    def Printname(self):
        print(self.Username, self.Password)

class Buyer(User):
    def __init__(self, Username, Password, Address, Nationalcode):
        super().__init__(Username, Password)
        self.Address = Address
        self.Nationalcode = Nationalcode

x = Buyer("hanishnsr", "1234", "qom", "0372377658")
print(x.Username)
print(x.Password)
print(x.Address)      
print(x.Nationalcode)
