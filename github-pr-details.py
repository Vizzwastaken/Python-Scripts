import requests  # Importing the requests library which is used to make HTTP requests

# URL of the GitHub API endpoint for the desired repository
url = 'https://api.github.com/repos/prometheus-community/stackdriver_exporter/pulls'

# Sending a GET request to the GitHub API endpoint
response = requests.get(url)

# Creating an empty dictionary to store user PR counts
entry = {}

if response.status_code == 200:
    # Converting the response data to JSON format
    pullrequests = response.json()

    # Iterating over each pull request in the response
    for pull in pullrequests:
        # Extracting the username of the pull request creator
        user = pull["user"]["login"]
        # Incrementing the PR count for the user in the 'entry' dictionary
        if user in entry:
            entry[user] += 1
        else:
            entry[user] = 1

    print("The list of users with PRs is:")
    for name, count in entry.items():
        print(f'{name} : {count}')
else:
    # If the response status code is not 200, print an error message
    print("Failed to fetch, error code: " + str(response.status_code))
