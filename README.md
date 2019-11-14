# containerinfo

## What is containerinfo ?

containerinfo is a Docker container that publishes information about itself over http port 5000. containerinfo is built using Python 3 and Flask.

The following informations will be shown:

- Container's current time (UTC)
- Hostname
- IP Address
- CPU count
- OS
- Distribution (not supported when using Alpine Linux as a base image)
- Architecture

## How to use containerinfo

Run the following command on your Docker host:

```bash
docker container run -d -p 8080:5000 eaksel/containerinfo
```

Once the container is running you can check the information about it using your web browser (<http://your_docker_host:8080>).

You can also use curl within your Docker host's shell (`curl localhost:8080`).
