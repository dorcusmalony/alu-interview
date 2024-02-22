guillaume@ubuntu:~/$ cat 0-main.py
#!/usr/bin/python3
def pascal_triangle(n):
    """
    Returns a list of lists representing Pascal's triangle up to the nth row.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # Start with the first row [1]

    for i in range(1, n):
        prev_row = triangle[-1]  # Get the previous row
        curr_row = [1]  # Start with 1 for the current row

        # Calculate the values for the current row
        for j in range(1, i):
            curr_row.append(prev_row[j-1] + prev_row[j])

        curr_row.append(1)  # Append 1 at the end of the row
        triangle.append(curr_row)  # Add the current row to the triangle

    return triangle
