
# Write a program to simulate the rolling of two dice for 5000 times, 
# count the occurrence of each outcome, and print the results as a two-column table.

# Hint: You may store the results in a list which can be initialized usingresults = [0 for x in range(11)] .

# Solution:

import random

results = [0 for x in range(11)]

total_trials = 5000
for _ in range(total_trials):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    outcome = dice1 + dice2
    results[outcome - 2] += 1

print("Outcome Occurrence")
for outcome, occurrence in enumerate(results, start=2):
    print(f"{outcome:2}       {occurrence}")

print(f"Total number of trials is {total_trials}.")
