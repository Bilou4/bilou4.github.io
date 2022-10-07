# Bruteforce

Brute-force attacks work by calculating every possible combination that could make up a password and testing it to see if it is the correct password. Be aware that, as the password's length increases, the amount of time, on average, to find the correct password increases exponentially.

## Hydra

Hydra: tool developed by THC (The Hacker's Choice), uses bruteforce attacks on different protocols


```sh
hydra -l root -x 1:9:aA1 [@IP] ssh
```

* l : user to test for
* x: the tested password will have between 1 and 9 characters with min and shift and numbers
* V : verbose

```sh
hydra -V -L usernames.txt -P pass.txt [@IP] [protocol] # performs the combinations between each word in the text files.
```


```sh
hydra [@Host] -V -L usernames.txt -P pass.txt http-get-form "path/to/the/form/:username=^USER^&password=^PASS^&Login:F-incorrect:H=cookie:PHPSESSID=[cookie];security=high"
```

Login = name of the button and repeat as long as it is incorrect

___
## John The Ripper (JTR)

### Default use

```sh
john --wordlist=[fichierWordList] [fichierACraquer] # To make a crack based on a wordList
```

```sh
john --list=formats # all hash types that can be cracked by JTR
```
### Crack /etc/shadow

```sh
cp /etc/passwd ./
cp /etc/shadow ./
unshadow passwd shadow > passwords
john passwords # automatic detection of the hash and starts cracking (press a key to know the evolution (except 'q' because it quits)
john -show passwords # in the folder where the crack is made => to check what has been found
```


### Recovering the passphrase of a private key

```sh
ssh2john id_rsa > hash.txt
```

___
## CeWL (Custom Wordlist Generator)

https://github.com/digininja/CeWL

Tools to create a list of words based on a URL.

```sh
cewl --depth 2 --min_word_length 5 --write docswords.txt https://example.com
```

___
## Bruteforce an argument of a program

If you need to bruteforce an argument of a program.
```sh
strings random.dic > list.txt
while read LINE; do ./program "$LINE"; done < list.txt
```
