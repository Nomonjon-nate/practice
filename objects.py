''' OBJECTS
    (1) What is object?
    (2) Iterable objects & RANGE
    (3) DICTIONARY
    (4) Error handling system
'''

import array  # package/module
import math   # package
from math import ceil
print("===== What is object =====")
# An object has state & method properties
# Everything is object in Python!

print(type('Hello World!'))
print(type(100))
print(type(True))
print(type(array))
print(type(math))

# Paradigm > Functional Programming & OOP
# OOP's 4 CONCEPTS > Abstraction | Encapsulation | Inheritence | Polimorphism
result1 = math.ceil(97.7)  # CALL
print("result1:", result1)

result2 = ceil(98.3)
print("result2:", result2)

print("===== Error handling system =====")
car_dict = dict(name="Toyota", year=2026, electric=True)

try:
    print("passed here")
    result = car_dict["origin"]
    print("result:", result)
except KeyError as err:
    print("No origin state property found:", err)
else:
    print("Executed successfully without errors")
finally:
    print("Final closing logic")
