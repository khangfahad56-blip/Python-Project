import math

class calculator_operation:

  def __init__(self):
    pass

  def add(self, x, y):
     return x + y
  
  def sub(self, x, y):
     return x - y
  
  def mult(self, x, y):
     return x * y
  
  def divid(self, x, y):
     return x / y
  
  def remember(self, x,y):
    return x // y
  
  def power(self, x,y):
    return x ** y
  
  def sqrt(self, x):
     return math.sqrt(self, x)
  
  def cube(self, x):
     return math.cube(self, x)
  
  def root(self, x,y):
    return  x ** (1/y)
    
calc = calculator_operation()

while True:

  x = float(input("Enter first number: "))
  y = float(input("Enter second number: "))
  print("Select operation.")
  print("1.Add")
  print("2.Subtract")
  print("3.Multiply")
  print("4.Divide")
  print("5.Remember")
  print("6.Power")
  print("7.Square root")
  print("8.Cube root")
  print("9.Root")
  print("10.Exit")
  choice = input("Enter choice(1/2/3/4/5/6/7/8/9/10): ")
  if choice == '1':
    z = calc.add(x,y)
    print(f"Result: {z:.02f}")
  elif choice == '2':
    z = calc.sub(x,y)
    print(f"Result: {z:.02f}")
  elif choice == '3':
    z = calc.mult(x,y)
    print(f"Result: {z:.02f}")
  elif choice == '4':
    z = calc.divid(x,y)
    print(f"Result: {z:.02f}")
  elif choice == '5':
    z = calc.remember(x,y)
    print(f"Result: {z:.02f}")
  elif choice == '6':
    z = calc.power(x,y)
    print(f"Result: {z:.02f}")
  elif choice == '7':
    z = calc.sqrt(x,y)
    print(f"Result: {z:.02f}")
  elif choice == '8':
    z = calc.root(x,y)
    print(f"Result: {z:.02f}")
  elif choice == '10':
    break
