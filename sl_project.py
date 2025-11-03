import math

def calculate_factorial(n):
    """
    Calculates the factorial of a non-negative integer.
    Wraps math.factorial().
    """
    return math.factorial(n)

def calculate_sin(degrees):
    """
    Calculates the sine of an angle given in degrees.
    Wraps math.sin() after converting degrees to radians.
    """
    radians = math.radians(degrees)
    return math.sin(radians)

def calculate_cos(degrees):
    """
    Calculates the cosine of an angle given in degrees.
    Wraps math.cos() after converting degrees to radians.
    """
    radians = math.radians(degrees)
    return math.cos(radians)

def calculate_tan(degrees):
    """
    Calculates the tangent of an angle given in degrees.
    Wraps math.tan() after converting degrees to radians.
    """
    radians = math.radians(degrees)
    return math.tan(radians)

def calculate_ln(n):
    """
    Calculates the natural logarithm (base e).
    Wraps math.log().
    """
    
    return math.log(n)

def calculate_log10(n):
    """
    Calculates the common logarithm (base 10).
    Wraps math.log10().
    """
   
    return math.log10(n)



def add(a, b):
    """Adds two numbers."""
    return a + b

def subtract(a, b):
    """Subtracts two numbers."""
    return a - b

def multiply(a, b):
    """Multiplies two numbers."""
    return a * b

def divide(a, b):
    """
    Divides two numbers.
    Returns an error string if division by zero.
    """
    if b == 0:
        return "Error: Cannot divide by zero."
    return a / b


def print_menu():
    """Prints the calculator's main menu."""
    print("\n" + "="*30)
    print(" 🐍 Python Scientific Calculator")
    print("="*30)
    print("Basic Operations:")
    print(" 1. Add (+)")
    print(" 2. Subtract (-)")
    print(" 3. Multiply (*)")
    print(" 4. Divide (/)")
    print("\nScientific Operations:")
    print(" 5. Sine (sin)")
    print(" 6. Cosine (cos)")
    print(" 7. Tangent (tan)")
    print(" 8. Natural Log (ln)")
    print(" 9. Log Base 10 (log)")
    print(" 10. Factorial (n!)")
    print("\n 0. Exit")
    print("="*30)

def main():
    """Runs the main calculator loop."""
    while True:
        print_menu()
        choice = input("Enter your choice (0-10): ")

        if choice == '0':
            print("Exiting calculator. Goodbye! 👋")
            break

        
        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                
                if choice == '1':
                    print(f"Result: {num1} + {num2} = {add(num1, num2)}")
                elif choice == '2':
                    print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
                elif choice == '3':
                    print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
                elif choice == '4':
                    print(f"Result: {num1} / {num2} = {divide(num1, num2)}")

            except ValueError:
                print("Invalid input. Please enter numeric values.")

        
        elif choice in ('5', '6', '7', '8', '9', '10'):
            try:
                if choice == '10': 
                    num = int(input("Enter a non-negative integer: "))
                else:
                    num = float(input("Enter the number: "))

                if choice == '5':
                    print(f"Result: sin({num}°) = {calculate_sin(num)}")
                elif choice == '6':
                    print(f"Result: cos({num}°) = {calculate_cos(num)}")
                elif choice == '7':
                    print(f"Result: tan({num}°) = {calculate_tan(num)}")
                elif choice == '8':
                    print(f"Result: ln({num}) = {calculate_ln(num)}")
                elif choice == '9':
                    print(f"Result: log10({num}) = {calculate_log10(num)}")
                elif choice == '10':
                    print(f"Result: {num}! = {calculate_factorial(num)}")

            except ValueError as e:
                
                print(f"Error: Invalid input. {e}")
        
        else:
            print("Invalid choice. Please select an option from 0 to 10.")


if __name__ == "__main__":
    main()
