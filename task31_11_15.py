#11: Lambda Functions
 #Task: Create a program that sorts a list of tuples by the second element using a lambda function.
def sort_by_second_element(tuples_list):
    return sorted(tuples_list, key=lambda x: x[1])  # Sorting by second element

tuples_list = [(1, 2), (3, 1), (5, 4)]

sorted_list = sort_by_second_element(tuples_list)
print("Sorted List:", sorted_list)

#12:Exception Handling
 #Task: Write a program that handles a division by zero error.

def safe_division(a, b):
    try:
        result = a / b
        print("Result:", result)
    except ZeroDivisionError:
        print("Cannot divide by zero.")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

safe_division(num1, num2)

#13:File Handling
 #Task: Write a program that reads a text file and counts the number of lines and words.

def count_lines_words(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines() 
            num_lines = len(lines)  
            num_words = sum(len(line.split()) for line in lines)  
            print(f"Number of lines: {num_lines}")
            print(f"Number of words: {num_words}")
    except FileNotFoundError:
        print("File not found. Please provide a valid file.")


filename = "sample.txt" 
count_lines_words(filename)

#14: Classes and Objects
 #Task: Create a class Car with attributes like make, model, and year. Add methods to display the car's information and to calculate the car's age.
from datetime import datetime

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car: {self.year} {self.make} {self.model}")

    def get_age(self):
        current_year = datetime.now().year
        return current_year - self.year

car1 = Car("Toyota", "Camry", 2015)

car1.display_info()

print("Car Age:", car1.get_age(), "years")

#15: Modules and Libraries
 #Task: Create a Python program that uses the math library to calculate the factorial of a given number.
import math

def calculate_factorial(n):
    return math.factorial(n)

n = int(input("Enter a number: "))

print(f"Factorial of {n} is:", calculate_factorial(n))
