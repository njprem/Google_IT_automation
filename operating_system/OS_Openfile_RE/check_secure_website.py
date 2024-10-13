import re

def secure_website_domain(website):
 pattern = r"^[a-z]+s.+\.([a-z]+)\.[a-z]*$" # enter the regex pattern here
 result = re.search(pattern, website) # enter the re method here
 if result is None:
  return ""
 return result[1]# enter the correct capturing group


print(secure_website_domain("http://www.text.com")) #Should return nothing
print(secure_website_domain("https://www.text.com")) #Should return text
print(secure_website_domain("http://www.text.co")) #Should return nothing
print(secure_website_domain("https://www.text.co")) #Should return text