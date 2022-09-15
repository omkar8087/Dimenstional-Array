from __future__ import print_function

user_input = raw_input("Enter values for row and column number: ")
rows, cols = user_input.split(",")
rows = int(rows)
cols = int(cols)

grid = []
for x in range(rows):
    row = []
    for y in range(cols):
        row.append(x * y)
    grid.append(row)
    print(row)

print()
print(grid)