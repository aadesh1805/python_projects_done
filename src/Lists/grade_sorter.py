# Lists: Grade Sorter

# Welcome message
print("Welcome!")

#Gets user input
grades = [int(input("Enter your grade: ")) for i in range(5)]

#Printing the grades
print(f"Your grades are {grades}")

# Prints the sorted list
print(f"Your grades from highest to lowest are {grades.sort(reverse = True)}")

# Drops lowest grades
print("The lowest two grades will now be dropped.")
for i in range(2): print(f"Removed grade: {grades.pop()}")

# Prints remaining grades
print(f"Your remaining grades are {grades}")
print(f"Good Job! Your highest grade is a {grades[0]}")
