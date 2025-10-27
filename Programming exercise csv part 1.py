import csv

def write_grades():
    # Create or overwrite grades.csv and write student data
    with open("grades.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        # Write header row
        writer.writerow(["First Name", "Last Name", "Exam 1", "Exam 2", "Exam 3"])

        # Ask user for number of students
        num_students = int(input("How many students do you want to enter? "))

        # Get student info
        for i in range(num_students):
            print(f"\nEntering data for student {i + 1}:")
            first = input("Enter first name: ")
            last = input("Enter last name: ")
            exam1 = int(input("Enter Exam 1 grade: "))
            exam2 = int(input("Enter Exam 2 grade: "))
            exam3 = int(input("Enter Exam 3 grade: "))

            # Write the row to the CSV file
            writer.writerow([first, last, exam1, exam2, exam3])

    print("\nAll data has been written to grades.csv successfully!")

# Run the function
if __name__ == "__main__":
    write_grades()