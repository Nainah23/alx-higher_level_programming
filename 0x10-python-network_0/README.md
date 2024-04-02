HTTP Request Bash Scripts
This project contains a set of Bash scripts designed to perform various HTTP requests using curl. Each script serves a specific purpose related to interacting with web servers and processing HTTP responses.

Scripts Overview:
0-body_size.sh: Displays the size of the body of an HTTP response in bytes.
1-body.sh: Retrieves and displays the body of an HTTP response if the status code is 200.
2-delete.sh: Sends a DELETE request to a URL and displays the body of the response.
3-methods.sh: Displays all HTTP methods accepted by the server for a given URL.
4-header.sh: Sends a GET request to a URL with a custom header and displays the body of the response.
5-post_params.sh: Sends a POST request to a URL with specified parameters and displays the body of the response.
100-status_code.sh: Displays only the status code of an HTTP response.
101-post_json.sh: Sends a JSON POST request to a URL with the contents of a file and displays the body of the response.
102-catch_me.sh: Makes a request to a specific URL that responds with a message containing "You got me!" in the body.
Usage:
To use these scripts, simply execute them from the command line, passing any required arguments as instructed in the script comments. Ensure that curl is installed on your system for proper execution.

Example:

Copy code
./0-body_size.sh example.com
Testing:
These scripts can be tested in a sandbox environment provided by running a web server on port 5000. Instructions for testing each script are provided in the script comments.

Notes:
These scripts are designed for educational purposes and may require modification for use in production environments.
Refer to the comments within each script for detailed usage instructions and requirements.
Feel free to explore and utilize these scripts for your HTTP request needs!
