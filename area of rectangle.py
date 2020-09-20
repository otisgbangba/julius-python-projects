class rectangle():
    def init(self,breadth,length):
        self.breadth = breadth
        self.length = length
    def area(self):
        return self.breadth * self.length
a = int(input("Enter length of rectangle:"))
b = int(input("Enter breadth of rectangle:"))
z = a * b
print(z)

