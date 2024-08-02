# pattern_drawing.py

# Prompt the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))
# Draw the pattern
row = 0
while row < size:
    # Print asterisks for the current row
    for _ in range(size):
        print("*", end="")
    # Move to the next line
    print()
    row += 1
