Tasks - Python Network Scripts
This repository contains a collection of Python scripts designed to perform various network-related tasks, such as making HTTP requests, interacting with APIs, and handling responses. Each script addresses a specific task outlined in the project requirements.

Project Structure:
Task Descriptions:
What's my status? #0: Fetches and displays the status of a specified URL using the urllib package.
Response header value #0: Retrieves and displays the value of the X-Request-Id variable in the header of an HTTP response using urllib.
POST an email #0: Sends a POST request with an email parameter to a specified URL and displays the response body using urllib.
Error code #0: Retrieves and displays the body of an HTTP response, handling urllib.error.HTTPError exceptions and printing the HTTP status code if it's an error.
What's my status? #1: Fetches and displays the status of a specified URL using the requests package.
Response header value #1: Retrieves and displays the value of the X-Request-Id variable in the header of an HTTP response using requests.
POST an email #1: Sends a POST request with an email parameter to a specified URL and displays the response body using requests.
Error code #1: Retrieves and displays the body of an HTTP response, printing the HTTP status code if it's an error, using requests.
Search API: Sends a POST request to search for a user based on a letter parameter, displays the user's id and name if found, and handles JSON formatting and errors.
My GitHub!: Uses Basic Authentication with a personal access token to access GitHub API and display the user's id based on provided credentials.
Time for an interview!: Retrieves and displays the latest commits of a specified repository by a given user using the GitHub API.
Usage:
Each script can be executed from the command line, and usage instructions are provided within the script comments. Ensure that the necessary packages are installed before running the scripts.

Example:

Copy code
python3 0-hbtn_status.py
Testing:
These scripts can be tested in various environments, including the provided sandbox, using the web server running on port 5000. Follow the instructions provided in the project description for testing each script.
