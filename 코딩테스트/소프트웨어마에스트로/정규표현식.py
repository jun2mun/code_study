import re

text = "I have two apples."
pattern = r'' + input()
print(pattern)
pattern = re.compile(pattern)
print(pattern)
result = re.findall(pattern, text)
print(result)