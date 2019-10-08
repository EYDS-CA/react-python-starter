# react-python-starter

Basic react+python app to be used as a starting point

## Installation and Usage

This file describes how to run the project and develop against it.
NOTE: The instructions below haven't been tested on windows. If you are using windows
it is recommended to use WSL (Windows Subsytem for Linux).

## Requirements

- Docker

## Getting Started

The project uses Make commands listed in the [Makefile](Makefile) for ease of development.

Please refer to [Makefile](Makefile) for a list of all commands. Some of the most common ones are listed as follows:

`make run` : Launch the application using docker (Builds the images if they haven't been built before)
`make build` : (Re-)Builds container images listed in the docker-compose.
`make clean` : Stops any running containers and deletes dangling images and volumes

NOTE: If you're having any unexpected issues, it's best to run `make rebuild` to cleanup and rebuild containers from scratch.

## Container Information

- The client container exposes port 3000 and can be viewed by visiting http://localhost:3000

## CI/CD

- The application uses Github Workflows to run CI/CD pipelines. For more information checkout the [Github Actions Readme](.github/workflows/README.md)

## License

Code released under the [Apache License, Version 2.0](LICENSE).
