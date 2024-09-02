
# Function: add_numbers
def add_numbers(num1, num2):
    """Add two numbers and return the result."""
    return num1 + num2

def test_add_numbers():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        print(f"Result: {add_numbers(num1, num2)}")
    except ValueError:
        print("Invalid input. Please enter valid numbers.")

# Function: is_even
def is_even(number):
    """Check if a number is even."""
    return number % 2 == 0

def test_is_even():
    try:
        number = int(input("Enter a number: "))
        print(f"Is the number even? {is_even(number)}")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

# Function: reverse_string
def reverse_string(text):
    """Reverse the given string."""
    return text[::-1]

def test_reverse_string():
    text = input("Enter a string: ")
    if text:
        print(f"Reversed string: {reverse_string(text)}")
    else:
        print("Invalid input. Please enter a non-empty string.")

# Function: count_vowels
def count_vowels(text):
    """Count the number of vowels in the string (case-insensitive)."""
    vowels = 'aeiouAEIOU'
    return sum(1 for char in text if char in vowels)

def test_count_vowels():
    text = input("Enter a string: ")
    if text:
        print(f"Vowel count: {count_vowels(text)}")
    else:
        print("Invalid input. Please enter a non-empty string.")

# Function: calculate_factorial
def calculate_factorial(n):
    """Calculate the factorial of a non-negative integer."""
    if not isinstance(n, int):
        raise TypeError("Input must be an integer.")
    if n < 0:
        raise ValueError("Cannot calculate factorial for negative numbers.")
    factorial = 1
    for i in range(2, n + 1):
        factorial *= i
    return factorial

def test_calculate_factorial():
    try:
        n = int(input("Enter a non-negative integer: "))
        print(f"Factorial: {calculate_factorial(n)}")
    except ValueError as e:
        print(e)
    except TypeError as e:
        print(e)
    except ValueError:
        print("Invalid input. Please enter a non-negative integer.")

# Function: apply_decorator
def decorator_func(func):
    """Decorator that prints a message before calling the original function."""
    def wrapper(*args, **kwargs):
        print("Decorator Applied")
        return func(*args, **kwargs)
    return wrapper

@decorator_func
def apply_decorator(func):
    return func()

def test_apply_decorator():
    try:
        apply_decorator(lambda: print("Function executed!"))
    except Exception as e:
        print(f"An error occurred: {e}")

# Sequences: Sort List of Tuples
def sort_by_age(list_of_tuples):
    """Sort a list of (name, age) tuples by age."""
    if not all(isinstance(t, tuple) and len(t) == 2 and isinstance(t[1], int) for t in list_of_tuples):
        raise ValueError("List must contain tuples with a name and an integer age.")
    return sorted(list_of_tuples, key=lambda x: x[1])

def test_sort_by_age():
    try:
        num_people = int(input("How many people? "))
        if num_people <= 0:
            print("Number of people must be positive.")
            return
        people = []
        for _ in range(num_people):
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            people.append((name, age))
        print(f"Sorted by age: {sort_by_age(people)}")
    except ValueError as e:
        print(e)
    except ValueError:
        print("Invalid input. Please enter valid integers.")

# Sets and Dictionaries: Merge Dictionaries
def merge_dicts(dict1, dict2):
    """Merge two dictionaries, summing values for common keys."""
    if not (isinstance(dict1, dict) and isinstance(dict2, dict)):
        raise TypeError("Both inputs must be dictionaries.")
    result = dict1.copy()
    for key, value in dict2.items():
        result[key] = result.get(key, 0) + value
    return result

def test_merge_dicts():
    try:
        dict1 = eval(input("Enter the first dictionary: "))
        dict2 = eval(input("Enter the second dictionary: "))
        if not (isinstance(dict1, dict) and isinstance(dict2, dict)):
            print("Both inputs must be dictionaries.")
            return
        print(f"Merged dictionary: {merge_dicts(dict1, dict2)}")
    except (SyntaxError, NameError):
        print("Invalid dictionary format. Please enter valid dictionaries.")
    except TypeError as e:
        print(e)

# Object-Oriented Programming: Class Creation
class Car:
    """A simple Car class with make, model, and year attributes."""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        """Print the car's details."""
        print(f"{self.year} {self.make} {self.model}")

def test_car_class():
    try:
        make = input("Enter the car's make: ")
        model = input("Enter the car's model: ")
        year = int(input("Enter the car's year: "))
        if year < 1886:  # The year when the first cars were made
            print("Invalid year. Please enter a valid year.")
            return
        car = Car(make, model, year)
        car.display_info()
    except ValueError:
        print("Invalid input. Please enter a valid year.")

# Run all tests
if __name__ == "__main__":
    print("Testing add_numbers function")
    test_add_numbers()
    
    print("\nTesting is_even function")
    test_is_even()
    
    print("\nTesting reverse_string function")
    test_reverse_string()
    
    print("\nTesting count_vowels function")
    test_count_vowels()
    
    print("\nTesting calculate_factorial function")
    test_calculate_factorial()
    
    print("\nTesting apply_decorator function")
    test_apply_decorator()
    
    print("\nTesting sort_by_age function")
    test_sort_by_age()
    
    print("\nTesting merge_dicts function")
    test_merge_dicts()
    
    print("\nTesting Car class")
    test_car_class()

