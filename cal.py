[200~def add(a, b):
      return a + b

  def subtract(a, b):
      return a - b

  def multiply(a, b):
      return a * b

  def divide(a, b):
      if b == 0:
          raise ValueError("Division by zero is not allowed!")
      return a / b

  def main():
      num1 = float(input("Enter first number: "))
      num2 = float(input("Enter second number: "))
      operator = input("Enter operation (+, -, *, /): ")

      if operator == '+':
          result = add(num1, num2)
      elif operator == '-':
          result = subtract(num1, num2)
      elif operator == '*':
          result = multiply(num1, num2)
      elif operator == '/':
          result = divide(num1, num2)
      else:
          print("Error: Invalid operator!")
          return

      print("Result: ", result)

  if __name__ == '__main__':
      main()



