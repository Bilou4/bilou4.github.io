# Google Dorks


## Summary

| Filter                                     | Description                                                  |
| :----------------------------------------- | :----------------------------------------------------------- |
| `allintext:"keyword"`                      | Searches for occurrences of all the keywords given.          |
| `intext:"keyword"`                         | Searches for the occurrences of keywords all at once or one at a time. |
| `inurl:"keyword"`                          | Searches for a URL matching one of the keywords.             |
| `allinurl:"keyword"`                       | Searches for a URL matching all the keywords in the query.   |
| `intitle:"keyword"`                        | Searches for occurrences of keywords in title all or one.    |
| `allintitle:"keyword"`                     | Searches for occurrences of keywords all at a time.          |
| `site:"www.google.com"`                    | Specifically searches that particular site and lists all the results for that site. |
| `filetype:"pdf"`                           | Searches for a particular file type mentioned in the query.  |
| `link:"keyword"`                           | Searches for external links to pages.                        |
| `numrange:321-325`                         | Used to locate specific numbers in your searches.            |
| `(before:2000-01-01 after:2001-01-01)`     | Used to search within a particular date range.               |
| `inanchor:rat` (allinanchor)               | This shows sites which have the key terms in links pointing to them, in order of the most links. |
| `allinpostauthor:"keyword"` (inpostauthor) | Exclusive to blog search, this one picks out blog posts that are written by specific individuals. |
| `related:www.google.com`                   | List web pages that are “similar” to a specified web page.   |
| `cache:www.google.com`                     | Shows the version of the web page that Google has in its cache. |


### Features

#### OR - AND

```
site:facebook.com | site:twitter.com
site:facebook.com & site:twitter.com
```

#### Include results

This will order results by the number of occurrences of the keyword.
```
-site:facebook.com +site:facebook.*
```

#### Exclude results

```
site:facebook.* -site:facebook.com
```

#### Synonyms

Adding a `~` to a word tells Google that you want it to bring back synonyms for the term as well. For example, entering `~set` will bring back results that include words like `configure`, `collection` and `change` which are all synonyms of `set`.
```
~set
```

#### Glob pattern (*)

Putting an asterisk in a search tells Google `I don’t know what goes here`. Basically, it’s really good for finding half remembered song lyrics or names of things.
```
site:*.com
```

## Tools

[https://github.com/Zarcolio/sitedorks](https://github.com/Zarcolio/sitedorks) : Search Google/Bing/Ecosia/DuckDuckGo/Yandex/Yahoo for a search term with a default set of websites, bug bounty programs or a custom collection.