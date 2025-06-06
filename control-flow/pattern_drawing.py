# pattern_drawing.py

# Prompt User for Pattern Size
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Draw the Pattern using while and for loop
while row < size:
    for col in range(size):
        print("*", end="")
    print()  # Move to the next line after printing one row
    row += 1
