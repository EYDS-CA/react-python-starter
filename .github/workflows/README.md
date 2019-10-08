# Github workflows

This application uses [Github Actions](https://github.com/features/actions) to run CI/CD and other workflows.

## Requirements

### Docker Hub

1. Create a registry for storing client images. (This will be `DOCKER_HUB_CLIENT_REPO` in the GITHUB step below)

### AWS

Create an EC2 instance on AWS with docker installed to run the application containers on. Note the private key and the public IP address needed to SSH into the instance. (This will be `AWS_EC2_SSH_KEY` and `AWS_INSTANCE_IP_ADDRESS` in the GITHUB step below)

### GITHUB

You need the following [Secrets](https://help.github.com/en/articles/virtual-environments-for-github-actions#creating-and-using-secrets-encrypted-variables) defined in your Github Repo for the deployment to run as expected.

`DOCKER_HUB_CLIENT_REPO` : Name of the container registry repository for the client to store/fetch images from.
`DOCKER_HUB_PASSWORD` : Username for authenticating against the container registry.
`DOCKER_HUB_USERNAME` : Password for authenticating against the container registry
`AWS_EC2_SSH_KEY` : Private key for SSH-ing into the ec2 instance.
`AWS_INSTANCE_IP_ADDRESS` : Public IP address of the ec2 instance.

## Workflows

The workflows have been divided per service on for two events (Push, Pull Request).

1. When a pull request is made, the CI part of the application kicks off. The definition can be found in the file `pull-request-xxx.yml` where xxx is the client/server.

2. When a merge/push is made to the master branch, the CD part of the application kicks off into place and deploys the application to whatever environment necessary. The definition can be found in the file `merge-to-master.yml`
