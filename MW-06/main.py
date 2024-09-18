# Define the maximum width of the pattern
max_width = 5

# Print the top half of the pattern
for i in range(1, max_width + 1):
    print(''.join(str(x) for x in range(1, i + 1)))

# Print the bottom half of the pattern
for i in range(max_width - 1, 0, -1):
    print(''.join(str(x) for x in range(1, i + 1)))