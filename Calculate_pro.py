print("\n\t***This is a Calculator Project***\n\n")
class cal:
    def add(self):
            print("This is the addition...")
            self.a=int(input("Enter the first value :"))
            self.b=int(input("Enter the second value :"))
            self.c=self.a+self.b
            print("The addition is :",self.c)
    def sub(self):
            print("This is the subtraction...")
            self.a=int(input("Enter the first value :"))
            self.b=int(input("Enter the second value :"))
            self.c=self.a-self.b
            print("The subtraction is :",self.c)
    def mul(self):
            print("This is the multiplication...")
            self.a=int(input("Enter the first value :"))
            self.b=int(input("Enter the second value :"))
            self.c=self.a*self.b
            print("The multiplication is :",self.c)
    def div(self):
            print("This is the division...")
            self.a=int(input("Enter the first value :"))
            self.b=int(input("Enter the second value :"))
            self.c=self.a/self.b
            print("The multiplication is :",self.c)
obj=cal()
while True:
        se=int(input('''
                Select the option...
                    1. Addition
                    2. Subtraction
                    3. Multiplication
                    4. Division
                    5. Exit()
                    ->:'''))
        if se==1:
          obj.add()
        elif se==2:
              obj.sub()
        elif se==3:
              obj.mul()
        elif se==4:
              obj.div()
        else:
              print("\n\t***Thanks***\n")
              break
    