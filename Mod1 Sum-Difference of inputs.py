#Module 1 Critical Thinking Assignment Part 1

print("Hello. Let's do some basic arithmetic.")
print("Give me two numbers and I will find the sum and difference of those numbers")

# Get input and make sure inputs are numeric
while True:
  num1 = (input("Enter the first number: "))
  try:
    num1 = float(num1)
    break
  except ValueError:
    print("Thats not a number")

while True:
  num2 = (input("Please enter a second number: "))
  try:
    num2 = float(num2)
    break
  except ValueError:
    print("Thats not a number")

num_sum = (num1 + num2)
num_diff = round(num1 - num2, 4)
#Rounding difference to 4 decimal places

print(f"{num_sum} is the sum of {num1} and {num2}")
print(f"and {num_diff} is the difference of {num1} and {num2}")
print("Thanks for playing!")


