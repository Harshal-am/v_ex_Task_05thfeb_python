#16: Recursion
# Task: Write a recursive function to calculate the factorial of a number.

def factorial(n):
    if n == 0 or n == 1:  
        return 1
    else:
        return n * factorial(n - 1)  

n = int(input("Enter a number: "))

print(f"Factorial of {n} is:", factorial(n))


# 17: Regular Expressions
# Task: Write a program to check if a given string is a valid email address using a regular expression.
import re

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(pattern, email):
        print("Valid email address.")
    else:
        print("Invalid email address.")

email = input("Enter an email address: ")

is_valid_email(email)

# 18: Working with Dates and Times
# Task: Write a program that displays the current date and time in the format: YYYY-MM-DD HH:MM:SS.
from datetime import datetime
current_time = datetime.now()

formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

print("Current Date and Time:", formatted_time)

# 19: Decorators
# Task: Write a decorator that measures the time taken to execute a function.
import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Record start time
        result = func(*args, **kwargs)  # Execute function
        end_time = time.time()  # Record end time
        print(f"Time taken: {end_time - start_time:.6f} seconds")
        return result
    return wrapper

@timing_decorator
def example_task():
    time.sleep(2)  
    print("Task completed!")

example_task()

#20: Web Scraping
#Task: Use the requests and BeautifulSoup libraries to scrape the titles of articles from a website (e.g., a news website).
import requests
from bs4 import BeautifulSoup

def scrape_titles(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  

        soup = BeautifulSoup(response.text, 'html.parser')

        titles = soup.find_all('h2')  

        print("Article Titles:")
        for title in titles:
            print("-", title.get_text(strip=True))
    
    except requests.exceptions.RequestException as e:
        print("Error fetching the webpage:", e)

url = "https://www.theguardian.com/us-news/2025/feb/04/trump-china-tariffs" 
scrape_titles(url)
