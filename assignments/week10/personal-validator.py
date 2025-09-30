"""
Create a Personal Information Validator program that:
    Asks user for their name, age, and phone number
    Validates that name contains only alphabetic characters and spaces
    Converts age from string to integer and validates it's between 18-65
    Validates phone number contains exactly 10 digits
    
    Uses appropriate string methods for validation
    Displays formatted output with proper string formatting
    
    USE: isalpha(), isdigit(), upper(), string formatting with % or .format()
    
Example Result

=== PERSONAL INFORMATION VALIDATOR ===
Enter your name: John Doe
Enter your age: 25
Enter your phone number: 9876543210

Validation Results:
Name: Valid (contains only letters and spaces)
Age: Valid (25 years old)
Phone: Valid (10-digit number)

Formatted Information:
Name: JOHN DOE
Age Group: Young Adult (18-30)
Phone: +91-9876543210

"""

print("=== PERSONAL INFORMATION VALIDATOR ===")
#name = input("Enter Your name :")
#age = int(input("Enter Your age :"))
#phone = input("Enter Your phone number :")

name = "John Doe"
age = 25
phone_number = "05555458256"

# name validation
nameFlag = True
for char in name :
    #print(char, char.isalpha())

    if char.isalpha() or char == " ":
        nameFlag = True
    else:
        nameFlag = False

ageFlag = True
if int(age) < 18 or int(age) > 65:
    ageflag = False

phoneFlag = True
if len(phone_number) != 10:
    phoneFlag = False
else:    
    for char in phone_number:
        if char.isdigit() == False:
            phoneFlag = False
            break
print("Validation Results:") 
if nameFlag:
    print("Name: Valid (contains only letters and spaces)")
else:
    print("Name: Invalid (not contains only letters and spaces)")

if ageFlag:
    #แบบที่1
    print(f"Age: Valid ({age} years old)")
    #แบบที่2
  # print("Age: Valid (%d years old)" % (int(age)))       
else:
    print("Age: Invalid (less than 18 or more than 65)")

if phoneFlag:
    print("Phone: Calid (10-digit number)")
else:
    print("Phone: Invalid (not 10-digit number)")

print("Formatted Information:")
print("Name:", name.upper(), name.lower() , name.capital())
if age >=18 and age <= 30:
    print("age Group: Young Adult (18-30)")
else:
    print("Age Group: not Young Adult")

print("Phone: +66-%s" (phone_number))