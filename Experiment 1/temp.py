import csv
import random
from datetime import datetime, timedelta

# Define the list of car names
car_names = [
    'Toyota Camry', 'Honda Accord', 'Ford Mustang', 'Chevrolet Malibu', 
    'Nissan Altima', 'BMW 3 Series', 'Audi A4', 'Mercedes-Benz C-Class', 
    'Hyundai Sonata', 'Kia Optima', 'Volkswagen Passat', 'Subaru Impreza'
]

# Generate random data for 30 days
num_days = 30
start_date = datetime.now()
data = []

for i in range(num_days):
    date = start_date + timedelta(days=i)
    day = date.strftime('%Y-%m-%d')
    cars_purchased = random.sample(car_names, k=random.randint(1, 3))  # Randomly select 1 to 3 cars purchased each day
    data.append([day, ', '.join(cars_purchased)])

# Write data to a CSV file
with open('automobiles.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Day', 'Cars Purchased'])
    writer.writerows(data)