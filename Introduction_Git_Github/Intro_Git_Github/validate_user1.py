#!/ust/bin/env python3


def validate_user(username, minlen):
    assert type(username) == str, "username must be a string"
    if not username.isalnum():
        return False
    return True



