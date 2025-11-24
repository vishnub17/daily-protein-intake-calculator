# Daily Protein Intake Tracker
# This program estimates weekly protein intake based on daily input

# Task 1: Welcome message
print("Welcome to the Daily Protein Intake Tracker!")

# Task 2: Asking the user for daily protein intake
protein_input = input("How many grams of protein did you eat today? ")

# Task 5: Converting input to float with error handling
try:
    protein = float(protein_input)
except ValueError:
    print("Please enter a valid number for protein intake.")
    exit()

# Task 3: Calculating weekly protein intake
weekly_protein = protein * 7

# Task 4: Displaying the result in a clear, readable format
print(f"\nGreat job! Based on today's intake, you are on track to consume about {weekly_protein} grams of protein this week.")
