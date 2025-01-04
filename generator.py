import csv
from faker import Faker

# Initialize Faker
fake = Faker()

# Define the number of rows
num_rows = 1000

# Create a CSV file
with open('persons.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    # Write the header
    writer.writerow(['first_name', 'last_name', 'dob', 'email'])
    
    # Generate and write rows
    for _ in range(num_rows):
        first_name = fake.first_name()
        last_name = fake.last_name()
        dob = fake.date_of_birth(minimum_age=18, maximum_age=90).strftime('%Y-%m-%d')
        email = fake.email()
        writer.writerow([first_name, last_name, dob, email])

print(f"Generated {num_rows} rows in 'persons.csv'")