x = 4

y = 5

x += 3

y *= 2

result = x / y


print(result)

a = 10
b = 4
c = 5

cond1 = a > b

cond2 = b % 2 == 0

cond3 = c <= a

#
final_condition = cond1 or (cond2 and cond3)


print(final_condition)

score = float(input("Enter the test score (0-100): "))

if score >= 90: 
    grade = "A"
elif score >= 80: 
    grade = "B"
elif score >= 70: 
    grade = "C"
elif score >= 60: 
    grade = "D"
else: 
    grade = "f"

print(f"the grade for a score of {score} is: {grade}\n")

num1 = float(input("enter the first number: "))
num2 = float(input("enter the second number: "))

operation = input("enter an operation(+, -, *, /) ")

result = None
error_message = None
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 == 0:
        error_message = "error: division by zero is not allowed"
    else:
        result = num1 / num2

else:
    error_message = "error: invalid operation entered."

if error_message:
    print(error_message)
else:
    print(f"the result is: {result}")                

