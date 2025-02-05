#1: Data Types and Variables
 #task - Create a Python program to convert temperatures between Celsius and Fahrenheit.
def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9

def main():
    print("Temperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    
    choice = input("Enter your choice (1 or 2): ")
    
    if choice == '1':
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")
    elif choice == '2':
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
    
#2:Strings and String Operations
 #Task - Write a program that checks if a word is a palindrome.
def is_palindrome(word):
    """Check if a word is a palindrome."""
    # Convert the word to lowercase to make the check case-insensitive
    word = word.lower()
    # Compare the word with its reverse
    return word == word[::-1]

def main():
    # Get input from the user
    word = input("Enter a word: ")
    
    # Check if the word is a palindrome
    if is_palindrome(word):
        print("Palindrome")
    else:
        print("Not Palindrome")

# Run the program
if __name__ == "__main__":
    main()
    
#3: Lists
 #Task: Create a program that takes a list of integers and returns the largest number in the list.
def find_largest_number(numbers):
    """Find the largest number in a list using a loop."""
    largest = numbers[0]  # Assume the first number is the largest
    for num in numbers:
        if num > largest:
            largest = num
    return largest

def main():
    # Input: A list of numbers
    numbers = [2, 3, 1, 4, 9]
 
    largest_number = find_largest_number(numbers)
    
    print("The largest number in the list is:", largest_number)

if __name__ == "__main__":
    main()
    
#4: Tuples
 #Task: Write a program that swaps the first and last elements of a tuple.
def swap_first_last(t):
    """Swap the first and last elements of a tuple."""
    lst = list(t)
    lst[0], lst[-1] = lst[-1], lst[0]
    return tuple(lst)

def main():

    t = (1, 2, 3, 4)
    
    swapped_tuple = swap_first_last(t)

    print("Original tuple:", t)
    print("Swapped tuple:", swapped_tuple)

if __name__ == "__main__":
    main()
    
#5: Dictionaries
 #Task: Write a program that counts the frequency of words in a sentence.
 
def word_frequency(sentence):
    words = sentence.split() 
    freq_dict = {}  
    
    for word in words:
        freq_dict[word] = freq_dict.get(word, 0) + 1 
    
    return freq_dict

sentence = "apple banana apple grape apple"
result = word_frequency(sentence)

print(result)
