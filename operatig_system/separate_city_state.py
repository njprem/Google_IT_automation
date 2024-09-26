import re

def parse_city_state(text):
 pattern = r"[a-z]+[,.]\s([a-z\s]+)" #enter the regex pattern here
 result = re.search(pattern, text,re.IGNORECASE) #enter the re method  here
 if result != None:
  return ""
 return result[1]#return the correct capturing group


print(parse_city_state("Hamilton, MN")) # should return MN
print(parse_city_state("Albuquerque, New Mexico")) # should return New Mexico
print(parse_city_state("Portland. Oregon")) # should return Oregon