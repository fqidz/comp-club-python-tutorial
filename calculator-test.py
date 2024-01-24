# Step 1
num1 = input("First number: ")
num2 = input("Second number: ")

# Step 2
num1 = int(num1)
num2 = int(num2)

# Step 3
operator = input("Operator: ")

# Step 4
if operator == "+":
    output = num1 + num2
elif operator == "-":
    output = num1 - num2
elif operator == "*":
    output = num1 * num2
elif operator == "/":
    output = num1 / num2
else:
    print("Input a valid operator.")

# Step 5
print(f"{num1} {operator} {num2} is equal to {output}")


# name = "Faidz"
# age = 17

# print(f"My name is {name} and I am {age} years old")



# # 1. print()
# # 2. Variables
# # 3. input()
# # 4. math
# # 5. Data Types (str, int, bool)
# # 6. Converting data types
# # 7. if statement
# # 8. f-strings

# # Get input from user & save it in variables
# # The input will be saved as a 'string'
# n1 = input("First number: ")
# n2 = input("Second number: ")
# operator = input("Operator: ")

# # Convert the input numbers from 'string' to 'integer'
# n1 = int(n1)
# n2 = int(n2)

# # Main logic
# # Checks what operator is used and does the corresponding calculation
# if operator == "+":
#     answer = n1 + n2
# elif operator == "-":
#     answer = n1 - n2
# elif operator == "*":
#     answer = n1 * n2
# elif operator == "/":
#     answer = n1 / n2
# else:
#     # Dont do any calculation if they input anything else other than '+', '-', '*', or '/'
#     print("Input a proper operation.")


# print(f"{n1} {operator} {n2} = {answer}")