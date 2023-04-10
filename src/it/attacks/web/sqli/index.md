# SQL injections

## Concept

* consists of sending data to an application that will generate a bug
* uses strings and interprets them as commands
* allows access and modification of the database

**Example**: `' OR 1=1 {option}; -- `

**{option}** can be:

```sql
select null, version()
select null, table_name from information_schema.tables # retrieve tables from the database
select null, column_name from information_schema.columns where information_schema.tables='[name]'
...
```

### Example

```go
// Correct format for executing an SQL statement with parameters.
rows, err := db.Query("SELECT * FROM user WHERE id = ?", id)

// SECURITY RISK!
rows, err := db.Query(fmt.Sprintf("SELECT * FROM user WHERE id = %s", id))
```

[source example](https://go.dev/doc/database/sql-injection)

## Tools

### SQLMAP

SQLMAP is a tool that automates the process of detecting and exploiting SQL injection flaws and taking over of database servers.

```bash
-u "url"
--cookie="PHPSESSID=.... ; security=low"
--dump # dump the database
```

## Protect yourself from it

* Escaping all user supplied input
* perform white list validation on user data
* minimize database privileges
* Use of Prepared Statements (with Parameterized Queries)

