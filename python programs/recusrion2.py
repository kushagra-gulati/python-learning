def find_uppercase_iterative(input_string):
    uppercase_letters = []  # Step 1
    
    for char in input_string:  # Step 2
        if char.isupper():    # Step 3
            uppercase_letters.append(char)  # Step 4
    
    return uppercase_letters  # Step 5

# Call the function and print the output
input_str = "Hello World"
result = find_uppercase_iterative(input_str)
print("Uppercase Letters:", result)
