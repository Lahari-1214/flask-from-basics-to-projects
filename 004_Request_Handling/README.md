### GET Request
##### Definition:
The GET method is used to retrieve data from the server.
It sends data through the URL (query string).
It is the default method when you open a web page or click a link.
##### Usage:
Used for reading or displaying data (not for changing it).
Parameters appear in the URL → not secure for sensitive data.
note: Data comes from query parameters using request.args.get()


### POST Request
##### Definition:
The POST method is used to send data securely to the server (e.g., form data).
Data is sent in the body of the request, not the URL.
Commonly used for form submissions or data insertion.
##### Usage:
Used for creating new data or sending confidential data.
Not visible in the URL → more secure.


