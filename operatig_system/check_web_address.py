import re

def check_web_address(text):
    # Corrected regex pattern
    pattern = r"[\w._]+\.[a-z]{2,}$"
    result = re.search(pattern, text, re.IGNORECASE)
    return result is not None

# Test cases
print(check_web_address("gmail.com"))               # True
print(check_web_address("www@google"))              # False
print(check_web_address("www.Coursera.org"))        # True
print(check_web_address("web-address.com/homepage")) # False
print(check_web_address("My_Favorite-Blog.US"))     # True