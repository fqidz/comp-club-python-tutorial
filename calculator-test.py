# 1. print()
# 2. Variables
# 3. input()
# 4. math
# 5. Data Types (str, int, bool)
# 6. Converting data types
# 7. if statement
# 8. f-strings

# Get input from user & save it in variables
# The input will be saved as a 'string'
n1 = input("First number: ")
n2 = input("Second number: ")
operator = input("Operator: ")

# Convert the input numbers from 'string' to 'integer'
n1 = int(n1)
n2 = int(n2)

# Main logic
# Checks what operator is used and does the corresponding calculation
if operator == "+":
    answer = n1 + n2
elif operator == "-":
    answer = n1 - n2
elif operator == "*":
    answer = n1 * n2
elif operator == "/":
    answer = n1 / n2
else:
    # Dont do any calculation if they input anything else other than '+', '-', '*', or '/'
    print("Input a proper operation.")


print(f"{n1} {operator} {n2} = {answer}")
