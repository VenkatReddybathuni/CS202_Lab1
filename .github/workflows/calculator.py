import sys

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            print("Error: Division by zero is not allowed.")
            return None
        return a / b

def main():
    calc = Calculator()
    
    print("Simple Calculator")
    print("Choose operation: 1. Add  2. Subtract  3. Multiply  4. Divide")
    
    try:
        choice = int(input("Enter choice (1/2/3/4): "))
        if choice not in [1, 2, 3, 4]:
            print("Invalid choice. Exiting program.")
            sys.exit(1)

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == 1:
            result = calc.add(num1, num2)
        elif choice == 2:
            result = calc.subtract(num1, num2)
        elif choice == 3:
            result = calc.multiply(num1, num2)
        elif choice == 4:
            result = calc.divide(num1, num2)

        print(f"Result: {result}")
    
    except ValueError:
        print("Error: Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()
