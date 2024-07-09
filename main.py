import csv
import json
from collections import defaultdict

# Text file operations
with open('files/example.txt', 'r') as file:
    l = file.readlines()
n = len(l)
print(f"Number of lines: {n}")
longest_line = max(l, key=len)
print(f"Longest line: {longest_line.strip()}")
reversed_lines = [line.strip()[::-1] for line in l]
print("Reversed lines:")
for line in reversed_lines:
    print(line)

# CSV file operations
with open('files/example.csv', 'r') as file:
    reader = csv.DictReader(file)
    data = list(reader)
    print(data)
total_age = sum(int(row['age']) for row in data)
print(f"Total age: {total_age}")
filtered_data = [row for row in data if int(row['age']) > 30]
print("Rows where age > 30:")
for row in filtered_data:
    print(row)
unique_cities = set(row['city'] for row in data)
num_unique_cities = len(unique_cities)
print(f"Number of unique cities: {num_unique_cities}")

# JSON file operations
with open('files/example.json', 'r') as file:
    data = json.load(file)
names = [person['name'] for person in data['people']]
print(f"Names: {names}")
total_age = sum(person['age'] for person in data['people'])
avg_age = total_age / len(data['people'])
print(f"Average age: {avg_age}")
people_by_city = defaultdict(list)
for person in data['people']:
    people_by_city[person['city']].append(person['name'])
print("People grouped by city:")
for city, names in people_by_city.items():
    print(f"{city}: {', '.join(names)}")
