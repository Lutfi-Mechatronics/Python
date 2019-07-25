

class LocalVariableMatha:
    def add(a=0, b=0):
        print(a+b)
    def subtract(a=0,b=0):
        print(a-b)
    def devide(a=0,b=0):
        print(a/b)

class ObjectMatha:
    def __init__(self, a=0,b=0):
        self.a=a
        self.b=b
    def add(self):
        print(self.a+self.b)
    def subtract(self):
        print(self.a-self.b)
    def devide(self):
        print(self.a/self.b)

class GlobalVariableMatha:
    a=0
    b=0
    def __init__(self, a=0,b=0):
        GlobalVariableMatha.a=a
        GlobalVariableMatha.b=b
    def add(self):
        print(GlobalVariableMatha.a+GlobalVariableMatha.b)
    def subtract(self):
        print(GlobalVariableMatha.a-GlobalVariableMatha.b)
    def devide(self):
        print(GlobalVariableMatha.a/GlobalVariableMatha.b)