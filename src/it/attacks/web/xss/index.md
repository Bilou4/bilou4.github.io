# XSS (Cross-Site Scripting) vulnerabilities

Allows an attacker to inject malicious client code into a website. This code is executed by victims and allows attackers to bypass access controls and impersonate users.

Corresponds to sending data to the victim in order to :
- Steal user sessions, sensitive data, rewrite the web page, redirect to a phishing site...
- Observe the client computer or even force the user to a particular site using an XSS proxy.


Example of a simple payload allowing to know if an input is vulnerable
```html
<script>alert(1)</script>
```

### Reflected XSS (not-persistent)
It is called non-persistent because it is not stored on the server (file or database). This type of XSS flaw does not store the malicious content on the web server. Instead, the content is delivered to the victim through a URL that contains it.



### Stored XSS (persistent)
The persistent XSS flaw is the most dangerous because it will be executed at each loading of the site. Indeed, the latter is stored either in a file or in a database. As an example, an attacker posts a comment on a discussion forum containing the malicious content. When other users go to the page containing the fraudulent message or comment, it will be executed.


## Protect yourself from it:
- Convert special characters to HTML entities (`htmlsepcialchars()`: Example `& → &amp; | " → &quot;`)
- Filter characters equivalent to html and js coding (`htmlentities()`)
- Remove tags
- Do not include user-supplied content in the output page

