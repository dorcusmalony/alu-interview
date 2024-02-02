# Project Name: rain_trapping

This project implements a solution to the "Rain Water Trapping" problem, calculating the amount of rainwater retained between walls represented by a list of non-negative integers.

###Functionality:

The rain function takes a list of non-negative integers representing wall heights and returns the total amount of rainwater trapped between them.
Handles edge cases like empty lists and non-wall ends.
Usage:

###Python
rain = __import__('0_rain').rain

walls = [0, 1, 0, 2, 0, 3, 0, 4]
print(rain(walls))  # Output: 6

walls = [2, 0, 0, 4, 0, 0, 1, 0]
print(rain(walls))  # Output: 6
Use code with caution. Learn more
Dependencies:

No external modules are used.
Documentation:

The 0_rain.py file includes docstrings for the rain function and any other functions implemented.
Coding Style:

PEP 8 (version 1.7.x) style guide is followed.
Executability:

All files are executable within the project directory.
Additional Notes:

Assumes non-negative integer wall heights represent a unit-width cross-section.
Water cannot overflow walls or flow past non-wall ends.
Author:
d.malony@alustudent.com

Visual Representation:

The example outputs represent the amount of rainwater trapped in the following wall configurations:

[0, 1, 0, 2, 0, 3, 0, 4] would trap 6 units of water.
[2, 0, 0, 4, 0, 0, 1, 0] would also trap 6 units of water.
