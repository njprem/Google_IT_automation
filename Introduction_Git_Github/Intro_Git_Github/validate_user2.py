#!/usr/bin/env python3

def validate_user(username, minlen):

    if minlen < 1:
        raise ValueError("minlen must be at least 1")

    if not username.isalnum():
        return False
    if username[0].isnumeric():    # Usernames can't begin with a number
        return False
    return True



