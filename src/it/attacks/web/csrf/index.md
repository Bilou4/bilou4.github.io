# CSRF (Cross Site Request Forgery)

The victim's browser generates a request to a vulnerable web application.

This vulnerability is caused by the ability of browsers to automatically send authentication data in each request.

**authentication data** :
* session cookie
* HTTP authentication header
* IP address
* client SSL certificate


## Protect yourself:
* add a token, not sent automatically, to all sensitive requests => this makes it impossible for the attacker to submit a valid request
* tokens must be cryptographically secure
* store a single token in the session and add it to all forms and links
