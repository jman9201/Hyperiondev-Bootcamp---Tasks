# Read data from DOB.txt
with open("DOB.txt", "r") as file:
    data = file.readlines()

# Splitting names and birthdates
names = []
birthdates = []
for line in data:
    parts = line.split()

    # Extracting name and birthdate from parts
    name = ' '.join(parts[:-3]) # Joining the 1st elements as name
    birthdate = ' '.join(parts[-3:]) # Joining the last 3 elements as birthdate

    # Adding name to names list
    names.append(name)

    # Adding birthdate to birthdates list
    birthdates.append(birthdate) 

# Print names
print("Full Name")
for name in names:
    print(name)

# Print birthdates
print("\nBirthdate")
for birthdate in birthdates:
    print(birthdate)

