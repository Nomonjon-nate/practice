''' FUNCTIONS
(1) DEFINE vs CAlL
(2) Parametr vs Argument
(3) Keyword & default arguments
(4) Scope
'''

print("====== DEFINE (parametr) vs CAlL (argument) =====")
# build in function > print() type()
# Function - reusable block of code!
# Instead of block {} in JAVA, Python uses INDENTATION!


# DEFINE - build; parametr
def greet(a):
    # define qismini yozish majburiy, hich bo'lmasa 'pass' yozib ketish kerak!
    print(f"How do you do {a}?")


def greeting(b):
    print("greeting is executed")
    return f"Hi {b}"


# CALL - execute; argument
result1 = greet('Nate')
print("result1:", result1)

result2 = greeting("Martin")
print("result2:", result2)


print("====== Keyword & default arguments =====")


def give_greet(name, age=22):
    print("give_greet is executed")
    return f"Hi {name}, you are {age} years old!"


result3 = give_greet(name="Justin", age=28)
print("result3:", result3)

result4 = give_greet("John")
print("result4:", result4)
