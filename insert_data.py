import csv
# from app import db
from models import DoctorModel

# Path to the CSV file
csv_file_path = 'api/data/Doctors.csv'

def insert_doctors_from_csv(file_path):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            doctor = DoctorModel(
                fee=float(row['Consultation Fee (INR)']),
                city=row['City'],
                email=row.get('Email', 'not provided'),
                address=row['Address'],
                state=row['State'],
                degree=row['Degrees'],
                contact=row.get('contact', 'not provided'),
                gender='Unknown',  # Gender not present in CSV, adjust as needed
                timings=row['day and timings'],
                hospital=row['Hospital'],
                username=row['Name'],  # Assuming Name will be used as username
                password='default_password',  # Set a default password, update later
                experience=row['Experience (years)'],
                qualification=row['Specialization']
            )
            # Hash the password before saving
            doctor.set_password('doctor')
            
            # Save to the database
            doctor.save()

# Call the function to insert data
insert_doctors_from_csv(csv_file_path)
