import json

USERS_FILE = "users.json"

def create_file():
    try:
        with open(USERS_FILE, "r"):
            pass 
    except FileNotFoundError: #pragma no cover
        with open(USERS_FILE, "w") as file:
            initial_data = []
            json.dump(initial_data, file, indent=4)

def read_from_file():
    try:
        with open(USERS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError: #pragma no cover
        return []

def write_to_file(data):
    with open(USERS_FILE, "w") as file:
        json.dump(data, file, indent=4)
    return "User added successfully."
