import re


# Function to validate phone numbers
def validate_phone(phone):
    """
    Validates phone numbers in formats:
    123-456-7890, (123) 456-7890, 1234567890, 123.456.7890
    """
    pattern = r'^(\(\d{3}\)|\d{3})[-.\s]?\d{3}[-.\s]?\d{4}$'
    return bool(re.match(pattern, phone))


# Function to validate Social Security Numbers
def validate_ssn(ssn):
    """
    Validates SSNs in format: 123-45-6789
    """
    pattern = r'^\d{3}-\d{2}-\d{4}$'
    return bool(re.match(pattern, ssn))


# Function to validate Zip Codes
def validate_zip(zip_code):
    """
    Validates US Zip Codes in formats: 12345 or 12345-6789
    """
    pattern = r'^\d{5}(-\d{4})?$'
    return bool(re.match(pattern, zip_code))


# Main function to test inputs
def main():
    print("=== Input Validation Program ===")

    phone = input("Enter your phone number: ")
    ssn = input("Enter your Social Security Number: ")
    zip_code = input("Enter your Zip Code: ")

    print("\nValidation Results:")
    print(f"Phone Number Valid: {validate_phone(phone)}")
    print(f"SSN Valid: {validate_ssn(ssn)}")
    print(f"Zip Code Valid: {validate_zip(zip_code)}")


if __name__ == "__main__":
    # Testing with a few examples
    print("Running tests...\n")
    test_data = {
        "Phones": ["123-456-7890", "(123) 456-7890", "1234567890", "123.456.7890", "123-45-678"],
        "SSNs": ["123-45-6789", "123456789", "12-345-6789"],
        "Zips": ["12345", "12345-6789", "1234", "123456"]
    }
    for category, values in test_data.items():
        print(f"\n{category} Tests:")
        for v in values:
            if category == "Phones":
                print(f"{v} -> {validate_phone(v)}")
            elif category == "SSNs":
                print(f"{v} -> {validate_ssn(v)}")
            elif category == "Zips":
                print(f"{v} -> {validate_zip(v)}")

    print("\n\nNow running main user input section...\n")
    main()
