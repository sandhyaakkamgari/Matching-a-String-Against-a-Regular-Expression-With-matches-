import re

pattern = r"^[a-zA-Z]+$"  # Matches a string of only letters
text = "Hello"

match = re.match(pattern, text)

if match:
  print("Match found!")
else:
  print("No match found.")