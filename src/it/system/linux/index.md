# Linux

## Namespace

This is the basis of docker. It allows you to simulate a network on your machine.

```bash
ip netns
ip netns add <NAME>
ip netns exec <NAME> <COMMAND> # execute a command in another namespace
```

