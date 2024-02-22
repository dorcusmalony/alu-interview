# [Pascal's Triangle]
This is a Python program that generates Pascal's Triangle up to a given number of rows. Pascal's Triangle is a triangular array of numbers that has many applications in various fields, including combinatorics, algebra, and probability theory.

## Description
The program defines a function pascal_triangle(n) that takes an integer n as input and returns a list of lists representing Pascal's Triangle up to the nth row. If n is less than or equal to 0, the function returns an empty list.

## [Usage]
To use this program, simply import the pascal_triangle function from the module and call it with the desired number of rows as an argument. Here's an example:

python


from pascal_triangle import pascal_triangle

# Generate Pascal's Triangle up to the 6th row
triangle = pascal_triangle(6)

# Print the triangle
for row in triangle:
    print(row)
This will output:


[1]
[1, 1]
[1, 2, 1]
[1, 3, 3, 1]
[1, 4, 6, 4, 1]
[1, 5, 10, 10, 5, 1]
You can also use the provided print_triangle function from the 0-main.py file to print the triangle in a formatted way


from pascal_triangle import pascal_triangle

def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))

# Generate Pascal's Triangle up to the 5th row
triangle = pascal_triangle(5)

# Print the formatted triangle
print_triangle(triangle)
This will output:



[1]
[1,1]
[1,2,1]
[1,3,3,1]
[1,4,6,4,1]
Algorithm
The pascal_triangle function uses the following algorithm to generate Pascal's Triangle:

Start with the first row [1].
For each subsequent row:
Get the previous row.
Start the current row with [1].
Calculate the values for the current row using the formula prev_row[j-1] + prev_row[j], where j goes from 1 to i-1 (the current row number minus 1).
Append 1 at the end of the current row.
Add the current row to the triangle list.
Return the triangle list.
The time complexity of this algorithm is O(n^2), and the space complexity is O(n^2), where n is the number of rows in the triangle.


