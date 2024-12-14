#!/usr/bin/env python3

import csv
import sys

def populatedictionary(filename):
  """Populate a dictionary with name/email pairs for easy lookup."""
  emaildict = {}
  with open(filename) as csvfile:
    lines = csv.reader(csvfile, delimiter = ',')
    for row in lines:
      name = str(row[0].lower())
      emaildict[name] = row[1]
  return emaildict

def find_email(argv):
  """ Return an email address based on the username given."""
  # Create the username based on the command line input.
  try:
    fullname = str(argv[1] + " " + argv[2])
    # Preprocess the data
    email_dict = populatedictionary('python_interact_with_OS/Python_Simple_Test/Email_Test/email.csv')
     # If email exists, print it
    if email_dict.get(fullname.lower()):
      return email_dict.get(fullname.lower())
    else:
      return "No email address found" 
  except IndexError:
    return "Missing parameters"

def main():
  print(find_email(sys.argv))
  print(find_email([None, "Blossom", "Gill"]))

if __name__ == "__main__":
  main()