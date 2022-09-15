# Program to validate the fields given in a form on Front End

# Validating the First name
while(True):
    firstname = input('Enter the first name: ')
    if len(firstname) < 3:
        print("First name must be 3 characters at least")
        continue
    if not firstname.isalpha():
        print("First name must be alphabetic characters")
        continue
    else:
        break

# Validating the Last name
while(True):
    lastname = input("Enter last name: ")
    if len(lastname) < 3:
        print("First name must be 3 characters at least")
        continue
    if not lastname.isalpha():
        print("First name must be alphabetic characters")
        continue
    else:
        break

# Validating the Age
while(True):
    age = input("Enter the age: ")
    if len(age) < 0:
        print("Age must not be empty")
        continue
    if not age.isdigit():
        print("Age must be a number")
        continue
    if int(age) < 14 or int(age) > 100:
        print("Age must be in range 14 to 100 years")
    else:
        break

# Validating the Phone number
while(True):
    phone = input("Enter the phone number: ")
    if len(phone) != 10:
        print("Phone number must be 10 characters long")
        continue
    if not phone.isdigit():
        print("Phone number must be digits")
        continue
    else:
        break

# Validating the City name
while(True):
    city = input("Enter the city name: ")
    if len(city) < 3:
        print("City name must be 3 characters long at least")
        continue
    if not city.isalpha():
        print("City name must be alphabetic characters")
        continue
    else:
        break

# Validating the Designation
while(True):
    designation = input("Enter the designation: ")
    if len(designation) <= 0:
        print("Designation must not be empty")
        continue
    if not designation.isalpha():
        print("Designation must be alphabetic characters")
        continue
    else:
        break

# Validating the Salary
while(True):
    salary = input("Enter Basic monthly salary: ")
    if len(salary) <= 0:
        print("Salary must not be empty")
        continue
    if not salary.isdigit():
        print("Salary must be numbers")
        continue
    if int(salary) < 5000:
        print("Salary must be more than Rs. 5000")
        continue
    else:
        break


print("firstname: {}".format(firstname))
print("lastname: {}".format(lastname))
print("age: {}".format(age))
print("phone number: {}".format(phone))
print("city: {}".format(city))
print("Designation: {}".format(designation))
print("Salary: {}".format(salary))

f = open("validationResults.txt", "w")
content = "First name: " + firstname + '\n' +\
            "Last name: " + lastname + '\n' +\
            "Age: " + age + '\n' +\
            "Phone Number: " + phone + '\n' +\
            "Designation: " + designation + '\n' +\
            "City: " + city + '\n' +\
            "Basic Salary: " + salary
f.write(content)
f.close()