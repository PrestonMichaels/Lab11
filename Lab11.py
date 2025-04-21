import matplotlib.pyplot as plt
import os
import re

def clean_input(input_str):
    # Remove extra spaces and convert to lowercase
    return re.sub('\s+', ' ', input_str).strip().lower()

# Replace input() with hardcoded values or mock inputs for testing
test_names = [("David", "M"), ("Emily", "F")]  # Add more names if needed

for name, sex in test_names:
    name = clean_input(name)
    sex = clean_input(sex)

    if sex not in ['m', 'f']:
        print("Invalid sex, please enter M or F")
        continue

    # Loop over all files from yob1880.txt through yob2021.txt
    years = []
    counts = []
    for year in range(1880, 2022):
        filename = f"names/yob{year}.txt"
        if not os.path.exists(filename):
            continue

        # Open the file and loop over all lines
        with open(filename, 'r') as f:
            for line in f:
                line = clean_input(line)
                parts = line.split(',')
                if len(parts) != 3:
                    continue
                line_name, line_sex, line_count = parts
                line_count = int(line_count)
                if line_sex != sex:
                    continue
                if line_name == name:
                    years.append(year)
                    counts.append(line_count)
                    break

    if not years:
        print(f"No {sex.upper()} babies named {name} found")
        continue

    plt.plot(years, counts)
    plt.title(f"Popularity of {name.capitalize()} vs year")
    plt.xlabel("Year")
    plt.ylabel("Count")
    plt.show()
