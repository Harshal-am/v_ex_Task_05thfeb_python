#6:Sets
 #Task: Write a program to find the intersection of two sets.

def find_intersection(set1, set2):
    return set1.intersection(set2)  

set1 = {1, 2, 3}
set2 = {2, 3, 4}

result = find_intersection(set1, set2)

print("Intersection:", result)

 
#7:If/Else Statements
#Task: Create a program that determines whether a given number is positive, negative, or zero.

def check_number(num):
    if num > 0:
        print("Positive")
    elif num < 0:
        print("Negative")
    else:
        print("Zero")

num = int(input("Enter a number: "))

check_number(num)


#8:Loops
#Task: Write a program that calculates the sum of all even numbers from 1 to a given number.

def sum_of_evens(n):
    return sum(num for num in range(2, n + 1, 2))  # Summing only even numbers

n = int(input("Enter a number: "))

print("Sum of even numbers:", sum_of_evens(n))

#9:Functions
# Task: Write a function that takes a list of numbers and returns the average of the list.
def calculate_average(numbers):
    if len(numbers) == 0:
        return 0  
    
    return sum(numbers) / len(numbers)  

numbers = [2, 4, 6, 8, 10]

print("Average:", calculate_average(numbers))

#10:List Comprehension
#Task: Write a program that generates a list of squares of numbers from 1 to 10 using list comprehension.

squares = [num ** 2 for num in range(1, 11)]

print("List of squares:", squares)
