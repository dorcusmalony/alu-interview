# alu-interview
## Minimum Operations to Reach 'n' Characters
### Problem Statement
In a text file, there is initially a single character 'H'. The text editor can execute only two operations: Copy All and Paste. Given a number 'n', the task is to write a method that calculates the fewest number of operations needed to result in exactly 'n' 'H' characters in the file.
Prototype
pythonCopy code
def minOperations(n: int) -> int 
Returns

An integer representing the minimum number of operations needed to achieve 'n' 'H' characters.
Constraints
If 'n' is impossible to achieve, return 0.
Example
pythonCopy code
n = 4 print("Min # of operations to reach {} char: {}".format(n, minOperations(n))) # Output: 4 n = 12 print("Min # of operations to reach {} char: {}".format(n, minOperations(n))) # Output: 7 
Instructions for Testing
Clone the repository:
bashCopy code
git clone <repository-url> 
Navigate to the project directory:
bashCopy code
cd minoperations 
Run the test script:
bashCopy code
./0-main.py 
View the output to verify that the implementation of minOperations is correct.
