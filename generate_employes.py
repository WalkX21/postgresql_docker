import csv
from faker import Faker

# Initialize Faker
fake = Faker()

# Define the number of rows
num_rows = 1000

# Define the output file path
output_file = 'employes.csv'

# Create a CSV file
with open(output_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Write the header
    writer.writerow(['Id', 'Nom', 'Age', 'Salaire'])
    
    # Generate and write rows
    for i in range(1, num_rows + 1):  # Start Id from 1
        Id = i
        Nom = fake.last_name() + ' ' + fake.first_name()  # Generate a full name
        Age = fake.random_int(min=18, max=65)  # Age between 18 and 65
        Salaire = round(fake.random_number(digits=5), 2)  # Salary with 2 decimal places
        writer.writerow([Id, Nom, Age, Salaire])

print(f"Generated {num_rows} rows in {output_file}")