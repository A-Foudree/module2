"""
Program: average_scores.py
Author: Ashley Fry
Last date modified: 01/24/2023
The purpose of this program is to write the manual tests and program average_scores.py to read
in one person's names, first and last, their age and three scores out of 100. Take the three scores
and find the average, storing into a variable.


It's time to write the main in your average_scores.py.
Prompt the user for what is expected for each input
Store into local variables last_name, first_name, age.
Use a constant to represent the number of scores you will prompt the user to input

Prompt the user for the scores, storing them in local variable or variables.
You can keep separate variables for each score, or you keep a running total in one variable.
Calcuate the average using the variables.
Print the output, with last name followed by a comma and the first name followed by an integer age
and then the average scores with 2 decimal places.
Example output:
Rodriguez, Linda age: 21 average grade: 92.50
Add doctring to the top of your file, add comments at the bottom with observed output after a few manual
 test runs of your code.
Submit your average_scores.py
"""

def main():
    last_name = input("Enter Last Name : ")
    first_name = input("Enter First Name : ")
    age = int(input("Enter your age : "))
    num_scores = 3
    score1 = int(input("Enter first score : "));
    score2 = int(input("Enter second score: "));
    score3 = int(input("Enter third score : "));
    avg = (score1 + score2 + score3)/num_scores;
    print(last_name,",",first_name,"age:",age,"average grade:%.2f"%avg)

if __name__ == "__main__":
    main()