# Disable Python formatter in Replit
import json

data = {}  # Default data

try:
    with open('.replit', 'r') as file:
        file_content = file.read()
        if file_content.strip():  # Check if the file is not empty
            data = json.loads(file_content)
            data['run'] = 'echo "Hello, World!"'
            data['language'] = 'python3'
        else:
            print(".replit file is empty. Using default data.")
except (json.JSONDecodeError, FileNotFoundError) as e:
    print(f"Error loading .replit file: {e}")
    # Handle the error or set default data

with open('.replit', 'w') as file:
    json.dump(data, file, indent=4)
