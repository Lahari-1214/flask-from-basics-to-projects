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


### PUT Request
##### Definition:
The PUT method is used to update or replace existing data on the server.
It’s common in RESTful APIs (not usually in HTML forms).
##### Usage:
Used when you want to update an existing resource.
Data is sent in the request body.

### DELETE Request
##### Definition:
The DELETE method is used to remove data from the server.
Often used in RESTful APIs to delete a resource.
##### Usage:
Deletes existing record(s) based on given ID or condition.



