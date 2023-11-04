# Quickly share your git repository

```admonish warning
This is an insecure (but very fast) way of sharing access to your git repository. Use only on a LAN where you know who can access your machine.
For a more secure way, use SSH.
```

## Read-only access

On the machine with the repository you want to share.
```bash
git daemon --base-path=/path/where/your/repositories/are --export-all --reuseaddr --informative-errors --verbose

# export-all - shares all the repositories in a folder from "–base-path" option
# base-path=. - daemon looks for repositories in a current directory(".")
# reuseaddr - allows to restart server quickly
# informative-errors - provides cleaner error message for clients
# verbose - notifies about each operation with the repository
```

```admonish info
With the previous example, all git repositories are exported because of the `export-all` option.
In order to manage which repository you want to share, simply create a `git-daemon-export-ok` empty file in the repository you want to share (and remove the former option).
```

On other machines
```bash
git clone git://IP/name-of-the-repository-to-clone
```

## Adding push access

To enable push access to your git repository, simply add `–enable=receive-pack` in your command line.

```admonish info
Before pushing, the client needs to create a new branch and push it to the server. Then you can merge it into the target branch.
```

## Creating aliases

Edit the `~/.gitconfig` file by adding the following lines

~~~admonish tip title="~/.gitconfig"
```toml
[alias]
    serve = !git daemon --base-path=. --export-all --reuseaddr --informative-errors --verbose
    hub = !git daemon --base-path=. --export-all --enable=receive-pack --reuseaddr --informative-errors --verbose
```
~~~

And use the newly created commands:

```bash
git serve
# or
git hub
```