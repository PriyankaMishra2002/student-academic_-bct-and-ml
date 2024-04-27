import pandas as pd
import numpy as np
import random
from faker import Faker
import hashlib  # Add this import statement
import json
from datetime import datetime

# Initialize Faker to generate fake data
fake = Faker()

# Define the number of entries
num_entries = random.randint(150, 200)

# Generate dummy data
data = {
    'student_id': [fake.unique.random_int(min=1000, max=9999) for _ in range(num_entries)],
    'name': [fake.name() for _ in range(num_entries)],
    'course': [fake.random_element(elements=('Computer Science', 'Mathematics', 'Physics', 'Biology')) for _ in range(num_entries)],
    'grade': [fake.random_element(elements=('A', 'B', 'C', 'D', 'F')) for _ in range(num_entries)],
    'age': [fake.random_int(min=18, max=25) for _ in range(num_entries)],
    'gender': [fake.random_element(elements=('Male', 'Female')) for _ in range(num_entries)],
    # Add more columns as needed
}

# Create a DataFrame
df = pd.DataFrame(data)

# Feature Engineering
# Example: Create a new feature for GPA based on grade
grades_to_gpa = {'A': 4.0, 'B': 3.0, 'C': 2.0, 'D': 1.0, 'F': 0.0}
df['gpa'] = df['grade'].map(grades_to_gpa)

# Simplified Blockchain
class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        return hashlib.sha256(str(self.index).encode() + 
                               str(self.timestamp).encode() + 
                               json.dumps(self.data).encode() + 
                               self.previous_hash.encode()).hexdigest()

# Create Blockchain
def create_blocks(df):
    blockchain = []
    for index, row in df.iterrows():
        data = {
            'student_id': row['student_id'],
            'name': row['name'],
            'course': row['course'],
            'grade': row['grade'],
            'age': row['age'],
            'gender': row['gender'],
            # Add more fields as needed
            'gpa': row['gpa']  # Include engineered features
        }
        if index == 0:
            previous_hash = "0"
        else:
            previous_hash = blockchain[-1].hash
        block = Block(index, datetime.now(), data, previous_hash)
        blockchain.append(block)
    return blockchain

blockchain = create_blocks(df)

# Print the first block as an example
first_block = blockchain[0]
print("Index:", first_block.index)
print("Timestamp:", first_block.timestamp)
print("Data:", first_block.data)
print("Previous Hash:", first_block.previous_hash)
print("Hash:", first_block.hash)
