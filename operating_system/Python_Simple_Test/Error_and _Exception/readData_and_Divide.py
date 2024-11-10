#!/usr/bin/env python3

def enhanced_read_and_divide(filename):
    try:
        with open(filename, 'r') as file:
            data = file.readlines()
        
        # Ensure there are at least two lines in the file
        if len(data) < 2:
            raise ValueError("Not enough data in the file.")
        
        num1 = int(data[0])  # Convert the first line to an integer
        num2 = int(data[1])  # Convert the second line to an integer
        
        # Check if second number is zero
        if num2 == 0:
            raise ZeroDivisionError("The denominator is zero.")
        
        return num1 / num2

    except FileNotFoundError:
        return "Error: The file was not found."
    except ValueError as ve:
        return f"Value error: {ve}"
    except ZeroDivisionError as zde:
        return f"Division error: {zde}"

# Example usage:
# filename = "data.txt"
# result = enhanced_read_and_divide(filename)
# print(result)