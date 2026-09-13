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
