from flask import Flask
import requests
from requests.auth import HTTPBasicAuth
import json

# Initialize the Flask application
app = Flask(__name__)

# Define a route for the createJira function, which will be accessible via a POST request
@app.route('/createJira', methods=['POST'])
def createJira():
    # JIRA API endpoint for creating a new issue
    url = "https://vishnucr7.atlassian.net/rest/api/3/issue"

    # Replace with your actual API token
    API_TOKEN = ""  

    # Set up the basic authentication with your email and API token
    auth = HTTPBasicAuth("vishnukalathilcr77@gmail.com", API_TOKEN)

    # Define the headers for the HTTP request
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    # Define the payload for the new JIRA issue, including the fields required by the API
    payload = json.dumps({
        "fields": {
            "description": {
                "content": [
                    {
                        "content": [
                            {
                                "text": "",  # Enter the description text for the JIRA ticket
                                "type": "text"
                            }
                        ],
                        "type": "paragraph"
                    }
                ],
                "type": "doc",
                "version": 1
            },
            "project": {
                "key": "SCRUM"  # Replace with your project key
            },
            "issuetype": {
                "id": "10001"  # Replace with the issue type ID
            },
            "summary": "",  # Enter the summary for the JIRA ticket
        },
        "update": {}
    })

    # Make the HTTP POST request to the JIRA API
    response = requests.request(
        "POST",
        url,
        data=payload,
        headers=headers,
        auth=auth
    )

    # Return the response from the JIRA API, formatted as JSON
    return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))

# Run the Flask app on the specified host and port
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
