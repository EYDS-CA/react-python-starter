# react-python-starter

Basic react+python app to be used as a starting point

Associated [Jira Epic](https://freshworks.atlassian.net/browse/WEB-92)

## Installation and Usage

This file describes how to run the project and develop against it.
NOTE: The instructions below haven't been tested on windows. If you are using windows
it is recommended to use WSL (Windows Subsytem for Linux).

This repo uses [git
submodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules). Due to this,
it is recommended that you use the following commands to setup the repo
locally.

Clone the repo and all of its submodules.

```
$ git clone --recurse-submodules git@github.com:FreshworksStudio/react-python-starter.git
```

Update the client submodule to latest `master`.
```
$ cd react-python-starter/client
$ git checkout master
$ git pull
```

## Requirements

- Docker

## Getting Started

The project uses Make commands listed in the [Makefile](Makefile) for ease of development.

Please refer to [Makefile](Makefile) for a list of all commands. Some of the most common ones are listed as follows:

`make run` : Launches the application using docker (Builds the images if they haven't been built before)

`make run-server` : Launches the server using docker (Builds the images if they haven't been built before)

`make stop` : Stops any running containers

`make build` : (Re-)Builds container images listed in the docker-compose.

`make clean` : Purges containers, images and volumes.

`make restart` : Stops the app, rebuilds the images and restarts the app.

`make server-test` : Runs the server unit tests.

`make client-test` : Runs the client unit tests.

NOTE: If you're having any unexpected issues, it's best to run `make rebuild` to cleanup and rebuild containers from scratch.

## Container Information

- The client container exposes port 3000 and can be viewed by visiting http://localhost:3000
- The server container exposes port 5000 and can be viewed by visiting http://localhost:5000
- The database container exposes port 5432 and can be viewed by using pgAdmin.

## CI/CD

- The application uses Github Workflows to run CI/CD pipelines. For more information checkout the [Github Actions Readme](.github/workflows/README.md)

## License

Code released under the [Apache License, Version 2.0](LICENSE).
