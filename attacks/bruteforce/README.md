## Bruteforce

### Hydra

Hydra : outil développé par THC (The Hacker's Choice), utilise des attaques brutes sur différents protocoles


```sh
hydra -l root -x 1:9:aA1 [@IP] ssh
```

* l : utilisateur pour lequel il faut tester
* x : les mdp testés auront entre 1 et 9 caractères avec min et MAJ et des chiffres
* V : verbose

```sh
hydra -V -L usernames.txt -P pass.txt [@IP] [protocol] # effectue les combinaisons entre chaque mot des fichiers textes.
```


```sh
hydra [@Host] -V -L usernames.txt -P pass.txt http-get-form "path/to/the/form/:username=^USER^&password=^PASS^&Login:F-incorrect:H=cookie:PHPSESSID=[cookie];security=high"
```

Login = nom du bouton et on répète tant que c'est incorrect

informations facilement récupérables avec burpSuite

<br>
<br>

___
### John The Ripper (JTR)

#### Utilisation par défaut

```sh
john --wordlist=[fichierWordList] [fichierACraquer] # Pour faire un crack basé sur une wordList
```

```sh
john --list=formats # tous les types de hash que peut craquer JTR
```
#### Cracker /etc/shadow

```sh
cp /etc/passwd ./
cp /etc/shadow ./
unshadow passwd shadow > passwords
john passwords # détection automatique du hash et commence à craquer (appuyer sur une touche pour connaitre l'évolution (sauf 'q' car cela quitte)
john -show passwords # dans le dossier où on effectue le crack => pour vérifier ce qui a été trouvé
```


#### Récupérer la passphrase d'une clé privée

```sh
ssh2john id_rsa > hash.txt
```

___
### CeWL (Custom Wordlist Generator)

https://github.com/digininja/CeWL

Tools to create a list of words based on a URL.

```sh
cewl --depth 2 --min_word_length 5 --write docswords.txt https://example.com
```

___
### Bruteforce an argument of a program

```sh
strings random.dic > list.txt
while read LINE; do ./program "$LINE"; done < list.txt
```
