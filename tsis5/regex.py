import re

text = "AdsBsaSdsa"
pattern1 = "ab*"
pattern2 = "ab{2,3}"
pattern3 = "[a-z]+_[a-z]+"
pattern4 = "[A-Z][a-z]+"
pattern5 = "^a.*b$"
pattern8 = "[A-Z][a-z]*"
matches = re.search(pattern5, text)

changed = re.sub("[., ]", ":", text)

snake_to_camel = ''.join(x.capitalize() or '_' for x in text.split('_'))

capitals_spaces = re.sub(r"(\w)([A-Z])", r"\1 \2", text)

split_by_upper = re.findall(pattern8, text)

camel_to_snake = re.sub(r"(\w)([A-Z])", r"\1_\2", text).lower()

print(camel_to_snake)
