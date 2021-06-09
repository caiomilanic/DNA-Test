from sys import argv, exit
import csv
import re

# Get arguments or print usage

if len(argv) != 3:
    print("Usage: python dna.py data.csv sequence.txt")
    exit(1)

# Open csv and txt sequence and read contents into memory

else:
    with open(f"{argv[1]}", newline='') as csvfile:
        database = csv.reader(csvfile)

    # Build a list of strings containing the STR patterns

        STR_list = next(database)

    with open(f"{argv[2]}", 'r') as txtfile:
        sequence = txtfile.read()

# For each STR in sequence, count longest run of consecutive repeats
    # For each position in the sequence: compute how many times the STR repeats starting at that position
        # For each position, keep checking successive substrings until the STR repeats no longer
        # Use len(s)
        # Use s[i:j] to return the substring of 's' with all chars from the ith chat up to jth (not including)

STR_list[:1] = []
Mirror_list = []

index = 0

for epoch in STR_list:

    STR = 1
    i = 0
    j = i + (len(STR_list[index]))

    for i in range(len(sequence)):

        if STR_list[index] not in sequence:

            STR = 0

        if sequence[i:j] == STR_list[index] and sequence[i+len(STR_list[index]):j+len(STR_list[index])] == STR_list[index]:

            STR += 1

        i += 1
        j += 1

# Save STR counts in some data structure (list or dict)

    Mirror_list.append(STR)

    index += 1

# Compare the STR counts against each row in the CSV
    # For each row in the data, check if each STR count matches
    # Use int() to turn string to an int


def str_list_to_int_list(str_list):
    n = 1
    while n < len(str_list):
        str_list[n] = int(str_list[n])
        n += 1
    return(str_list)


match = 0

with open(f"{argv[1]}", newline='') as csvfile:
    database_raw = csv.reader(csvfile)
    next(database_raw)

    for row in database_raw:
        row_int = str_list_to_int_list(row)

        if row[1:] == Mirror_list:
            match += 1
            print(row[0])

if match != 1:
    print("No match.")

print(Mirror_list)
print(STR_list)