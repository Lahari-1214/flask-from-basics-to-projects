## Why do we need State Management?
When we build a web application, communication between Client (Browser) and Server happens using HTTP protocol.
But HTTP is a stateless protocol.


####  Stateless means:
The server does NOT remember who you are.
Every request looks like it is coming from a new user, even if it is the same user.
So if the user logs in and then goes to another page, the server forgets the user login data.

### State Managements are 2 types:
1) Client-Side State Management (Cookies)
Cookies are stored in the browser
Data is visible to user
Can be modified by user
Used for: Remember username, language, small preferences

2) Server-Side State Management (Sessions)
Data is stored on server
Safer and more secure
Used for: login session, cart session, user data, etc.

