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
    student_grades = {
        "john archer": 68,
        "sofia appleman": 69,
        "hannah cheeseman": 69,
        "david cowman": 72
    }

    assignment_stats = {
        "lab 1": {
            "min": 59,
            "avg": 71,
            "max": 86
        },
        "project 1": {
            "min": 60,
            "avg": 71,
            "max": 87
        },
        "exam 1": {
            "min": 64,
            "avg": 72,
            "max": 84
        }
    }

    print("1. Student grade")
    print("2. Assignment statistics")
    print("3. Assignment graph")
    selection = input("\nEnter your selection: ")

    if selection == "1":
        name = input("What is the student's name: ")
        cleaned_name = clean_input(name)
        if cleaned_name in student_grades:
            print(f"{student_grades[cleaned_name]}%")
        else:
            print("Student not found.")

    elif selection == "2":
        assignment = input("What is the assignment name: ")
        cleaned_assignment = clean_input(assignment)
        if cleaned_assignment in assignment_stats:
            stats = assignment_stats[cleaned_assignment]
            print(f"Min: {stats['min']}%")
            print(f"Avg: {stats['avg']}%")
            print(f"Max: {stats['max']}%")
        else:
            print("Assignment not found.")

    elif selection == "3":
        name = input("What is the student's name: ")
        sex = input("What is the student's birth sex (M/F): ")
        baby_name_graph(name, sex)

    else:
        print("Other options not yet implemented.")

main()
