
from pymongo import MongoClient

# Connect to local MongoDB server
client = MongoClient("mongodb://localhost:27017/")

# Select database
db = client["HospitalDB"]

# Select collections
patients = db["patients"]
doctors = db["doctors"]
appointments = db["appointments"]


# Advanced DBMS: Create indexes
patients.create_index("phone")
appointments.create_index("doctor_id")
appointments.create_index([("date", 1), ("status", 1)])

print("Database indexes created successfully!")


# Test connection
try:
    client.admin.command("ping")
    print("MongoDB connected successfully!")
except Exception as e:
    print("MongoDB connection failed:", e)
