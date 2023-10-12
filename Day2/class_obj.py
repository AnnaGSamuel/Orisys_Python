'''Classes & objects'''
class MyClass:
    x = 5 
    def __init__(self,col): 
        self.color = col 
obj1 = MyClass(2)
obj2 = MyClass(3)
print(obj1.x)
print(obj2.color)