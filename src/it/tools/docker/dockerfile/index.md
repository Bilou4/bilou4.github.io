# Dockerfile

## Multi-stage build

Get a minimalist container simply running a binary. This helps keep the running docker container small while still be able to compile a project needing a lot of dependencies.

```dockerfile
# Step 1
FROM golang:alpine3.7 as build-env # Create an alias
COPY main.go /hello/main.go
WORKDIR /hello
RUN env GOOS=linux GOARCH=amd64 go build

# Step 2
FROM scratch
COPY --from=build-env /hello/hello /bin/hello # copy the compiled file from the build-env image
ENTRYPOINT ["/bin/hello"]
```

```bash
docker build -t hello-scratch:v1 . # build your image with the Dockerfile in the current directory
docker images # check you have your newly created image
docker run hello-scratch:v1 # run your image
```

[Official documentation for the multi-stage](https://docs.docker.com/build/building/multi-stage/)