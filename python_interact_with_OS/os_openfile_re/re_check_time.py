import re

def check_time(text):
    # Corrected regex pattern
    pattern = r"^(1[0-2]|0?[1-9]):([0-5][0-9])\s?(AM|PM|am|pm)$"
    result = re.search(pattern, text)
    return result is not None

# Test cases
print(check_time("12:45pm"))    # True
print(check_time("9:59 AM"))    # True
print(check_time("6:60am"))     # False (invalid minutes)
print(check_time("five o'clock")) # False (not numeric)
print(check_time("6:02 am"))    # True
print(check_time("6:02km"))     # False (invalid AM/PM)