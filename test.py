import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Fetching the service account key JSON file
cred = credentials.Certificate("serviceKey.json")
firebase_admin.initialize_app(cred, {
    "databaseURL": "https://test-75212-default-rtdb.firebaseio.com"
})

# Saving the data
ref = db.reference("test-data/")
users_ref = ref.child("users")

# Create
users_ref.set({
    "ID0001": {
        "Name": "Aaron",
        "Class:": "3rd Year"
    },
    "ID0002": {
        "Name": "Mark",
        "Class:": "4th Year"
    }
})

# Update
users_ref.update({
    "ID0001": {
        "Name": "Aaron",
        "Class:": "1st Year"
    }
})

# Delete
handle = db.reference("test-data/users/ID0004")
handle.delete()

# Read data
ref_read = db.reference("test-data/users/")
print(ref_read.get())