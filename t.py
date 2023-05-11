import re

def has_invalid_element(lst):
    pattern = r'^\d+(\.\d+)?$'
    for item in lst:
        if not re.match(pattern, str(item)):
            return True
    return False

lst = [1, '2', '3.14123123', '4.0', '5.1']
if has_invalid_element(lst):
    print("The list contains invalid elements.")
else:
    print("The list is valid.")
