# Git

## Specific topics

- [Quickly share your git repository](./git-daemon.md)

## Basic commands

- Cancel last local commit

```bash
git reset HEAD~1
```

-Remove a file from the index without deleting it

```bash
git reset HEAD <filename> # does not delete the file but removes it from the index
```

- Create new branch

```bash
git branch <branchName> # locally
# upstream branch
git branch --set-upstream-to=origin/<branchName>
git push -u origin <branchName>
```


- Merge some commits together

```bash
git rebase -i HEAD~X
# X = number of commits to merge
# 1. make your modification
# 2. if commits were already pushed: git push --force
# 3. else: git push
```

- Unstagged files and change active branch

```bash
git stash push -m "message"
git stash list
git checkout <another branch>
git stash pop
```

- Delete file from git history

```bash
git filter-branch --index-filter "git rm -rf --cached --ignore-unmatch <path-to-file>" HEAD
git push -all --force
```

- Find file in git history

```bash
git log --all --full-history -- <path-to-file>
```

- Apply commits on another branch

```bash
git cherry-pick <commit-hash>
```

- Add & push tags

```bash
git tag <tag-name>
git push --tags
```


- Use GIT with a GUI

```bash
gitk --all
```

