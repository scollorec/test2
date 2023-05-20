import test as test
import os
import json
"""
# Load the secret into a string
my_json_string = os.environ['GOOGLE_API_KEY']

# Parse the string back into JSON
my_json = json.loads(my_json_string)

# Now we can write this JSON object to a file
with open('output_file.json', 'w') as f:
    json.dump(my_json, f)

os.environ["GOOGLE_API_KEY"] = 'output_file.json'
"""

print(f"api_key_json: {os.environ['GOOGLE_API_KEY']}")

test.test()



