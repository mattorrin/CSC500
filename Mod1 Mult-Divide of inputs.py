#Module 1 Critical Thinking Assignment Part 2

print("Hello. Let's do some basic Math.")
print("Give me two numbers and I will multiply and divide those numbers")

# Get input and make sure inputs are numeric

while True:
  num1 = (input("Enter the first number: "))
  try:
    num1 = float(num1)
    break
  except ValueError:
    print("Thats not a number")

while True:
  num2 = (input("Please enter a second, non-zero, number: "))
  try:
    num2 = float(num2)
    break
  except ValueError:
    print("Thats not a number")

   
# Ensure the second number is non-zero to avoid division error
while True:
  if num2 != 0:
    print(f"Good!  You gave me {num1} and {num2}")
    break

  else:
    num2 = float(input("You cannot divide by 0! Please enter a second, non-zero, number: "))

#Rounding to 4 decimal places   
num_product = round(num1 * num2, 4)
num_quotient = round(num1 / num2, 4)


print(f"The product of {num1} and {num2} is {num_product}")
print(f"The quotient of {num1} and {num2} is {num_quotient}")

    



    
