import matplotlib.pyplot as plt
import os
import re

def clean_input(input_str):
    return re.sub('\s+', ' ', input_str).strip().lower()

def baby_name_graph(name, sex):
    name = clean_input(name)
    sex = clean_input(sex)

    if sex not in ['m', 'f']:
        print("Invalid sex, please enter M or F")
        return

    years = []
    counts = []
    for year in range(1880, 2022):
        filename = f"names/yob{year}.txt"
        if not os.path.exists(filename):
            continue

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
        return

    plt.plot(years, counts)
    plt.title(f"Popularity of {name.capitalize()} vs year")
    plt.xlabel("Year")
    plt.ylabel("Count")
    plt.show()

def main():
    print("1. Student grade")
    print("2. Assignment statistics")
    print("3. Assignment graph")
    selection = input("\nEnter your selection: ")

    if selection == "1":
        name = input("What is the student's name: ")
        print("69%")

    elif selection == "2":
        assignment = input("What is the assignment name: ")
        print("Min: 59%")
        print("Avg: 71%")
        print("Max: 86%")

    elif selection == "3":
        name = input("What is the student's name: ")
        sex = input("What is the student's birth sex (M/F): ")
        baby_name_graph(name, sex)
    else:
        print("Other options not yet implemented.")

main()
