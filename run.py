# Dunder __builtins__, __init__
message = "PYTHON: Everything is object!"
print(message)

result = type(message)
print("result:", result)

''' In Python, there are builtin methods:
(1) TYPES > int(integer) float str(string) list dict(dictionary)
(2) FUNCTION > print() len() input() type() str() int()
(3)CONSTANTS > True False None
'''

print(dir(__builtins__))
