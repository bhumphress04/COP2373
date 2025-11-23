import numpy as np
import csv

def load_data(filename):
    """
    Loads CSV file and returns a NumPy array containing ONLY exam scores.
    Assumes CSV has: First Name, Last Name, Exam 1, Exam 2, Exam 3
    """
    exam_rows = []

    with open(filename, newline='') as file:
        reader = csv.DictReader(file)

        for row in reader:
            # Convert ONLY exam values to floats
            exam_rows.append([
                float(row["Exam 1"]),
                float(row["Exam 2"]),
                float(row["Exam 3"])
            ])

    return np.array(exam_rows)


def print_stats_per_exam(data):
    num_exams = data.shape[1]

    print("\n=== Statistics Per Exam ===")
    for i in range(num_exams):
        exam = data[:, i]
        print(f"\nExam {i+1}:")
        print(f"  Mean:   {np.mean(exam):.2f}")
        print(f"  Median: {np.median(exam):.2f}")
        print(f"  Std:    {np.std(exam):.2f}")
        print(f"  Min:    {np.min(exam):.2f}")
        print(f"  Max:    {np.max(exam):.2f}")


def print_overall_stats(data):
    all_grades = data.flatten()

    print("\n=== Overall Statistics (All Exams Combined) ===")
    print(f"Mean:   {np.mean(all_grades):.2f}")
    print(f"Median: {np.median(all_grades):.2f}")
    print(f"Std:    {np.std(all_grades):.2f}")
    print(f"Min:    {np.min(all_grades):.2f}")
    print(f"Max:    {np.max(all_grades):.2f}")


def print_pass_fail(data):
    num_exams = data.shape[1]

    print("\n=== Pass/Fail Per Exam (60+ = Pass) ===")
    total_grades = 0
    total_passes = 0

    for i in range(num_exams):
        exam = data[:, i]

        passes = np.sum(exam >= 60)
        fails = np.sum(exam < 60)

        total_grades += len(exam)
        total_passes += passes

        print(f"\nExam {i+1}:")
        print(f"  Passed: {passes}")
        print(f"  Failed: {fails}")

    # Overall pass percentage
    pass_percentage = (total_passes / total_grades) * 100
    print(f"\nOverall Pass Percentage: {pass_percentage:.2f}%")



def main():
    filename = "grades.csv"
    data = load_data(filename)

    print("First few rows of the dataset (numeric exam columns only):")
    print(data[:5])

    print_stats_per_exam(data)
    print_overall_stats(data)
    print_pass_fail(data)


if __name__ == "__main__":
    main()
