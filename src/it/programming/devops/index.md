# Devops



## Git flow vs Github flow vs Gitlab flow

### Git flow

1. Main branch: holds the production code
2. develop branch: created from the main branch
3. feature branch: these are created from the develop branch (feature/notification; feature/buy...)
4. release branch: the branch that will be sent off to the main branch. Forked from develop.
5. hotfix branch: created from the main branch, used to fixed production, emergencies errors.

### Github flow

1. main branch: where the live production code stays
2. feature branch: every other branch (where developers work from) which are pulled off from the main branch. Once a featured is completed, a `pull request` is opened to the main branch, and after the proper testing, it is merged with the main branch.

### Gitlab flow

TODO