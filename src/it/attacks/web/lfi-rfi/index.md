# LFI & RFI

## LFI

allows a user to inject local files from a vulnerable URL

### Examples

```sh
url...?page=include.php # replace include.php with a server file
url...?page=/etc/passwd
```

### Include flaw

`<?php include('config.php'); ?>`

**Can be exploited in** :
* Local File Include (a local file to the server)
* Remote File Include (a shell)

#### Protect yourself from this:
* make sure that the pages you include are on your server
* function: file_exists('name');
* configuration .HTACCESS


### Faulty upload

Allows you to backdoor a server by executing a server-side script

**Can be exploited in** :
* double extension: `shell.php.jpg`;
* bypass mime verification: change the name of the script
* bypass mime verification: change the type of file being uploaded
* Selecting the destination directory

#### Protecting yourself:

* Rename files with random names and without extension
* Do not use the characters `< > ? & ;` but watch out for their equivalent in other encodings (urlencoding, ascii...)
* limit the case => forbid the execution of critical functions at the server level
* .HTACCESS configuration


### RFI

allows to include a remote file (mainly shell - command execution...)


```sh
url...?page=include.php

url...?page=http://www.google.fr # will add the google page to the page
```
