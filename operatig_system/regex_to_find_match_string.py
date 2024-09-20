import re  #regular expression library

log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"  # string
regex = r"\[(\d+)\]"         # r mean raw string so [] dont have to use double slash and (\d) use to match digit + is 1 or more than 1
result = re.search(regex, log)     #use regex to find matching object in log 
print(result[1])                #result[1] = 12345 result[0] = [12345]