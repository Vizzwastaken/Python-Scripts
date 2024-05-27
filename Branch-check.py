import requests
import re

# Define the URL of the GitHub API endpoint
url = 'https://api.github.com/repos/newrelic/helm-charts/branches'

# Define the regular expression pattern to match branch names
pattern = re.compile(r'renovate-*|master')

# Send a GET request to the GitHub API endpoint
response = requests.get(url)

# Parse the JSON response
content = response.json()

# Iterate over each branch in the response
for pull in content:
    # Check if the branch name matches the pattern
    if pattern.search(pull["name"]):
        print("Valid Branch Name : " + str(pull['name']))
    else:
        print("Invalid Branch Name : " + str(pull["name"]))
