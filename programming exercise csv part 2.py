import csv

def read_grades():
    # Open and read grades.csv
    with open("grades.csv", mode="r") as file:
        reader = csv.reader(file)
        header = next(reader)  # Skip header row

        # Print header with formatting
        print(f"{header[0]:<15}{header[1]:<15}{header[2]:<10}{header[3]:<10}{header[4]:<10}")
        print("-" * 60)

        # Print each student’s record
        for row in reader:
            print(f"{row[0]:<15}{row[1]:<15}{row[2]:<10}{row[3]:<10}{row[4]:<10}")

# Run the function
if __name__ == "__main__":
    read_grades()
