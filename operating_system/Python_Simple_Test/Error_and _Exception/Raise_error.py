my_list = [27, 5, 9, 6, 8]

def RemoveValue(myVal):
    if myVal not in my_list:
        raise ValueError("")
    else:
        my_list.remove(myVal)
    return my_list

print(RemoveValue(27))