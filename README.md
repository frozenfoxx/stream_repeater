# stream_repeater

[![Build Status](https://cloud.drone.io/api/badges/frozenfoxx/stream_repeater/status.svg?ref=refs/heads/main)](https://cloud.drone.io/frozenfoxx/stream_repeater)

Convert, upload, and post audio and video streams to remote services.

Docker Hub: [https://hub.docker.com/r/frozenfoxx/stream_repeater](https://hub.docker.com/r/frozenfoxx/stream_repeater)

# Build

## Docker

To build the Docker container run the following:

```
git clone https://github.com/frozenfoxx/stream_repeater.git
cd stream_repeater
docker build . -t 'frozenfoxx/stream_repeater:latest'
```

# Usage

## Docker

To load the application launch the container with your configuration:

```
docker run \
  -it \
  --rm \
  -v [mount point]:/data \
  -e CONFIG=[path to mounted config file] \
  -p 5000:5000 \
  frozenfoxx/stream_repeater:latest
```

Then access [http://localhost:5000](http://localhost:5000). If a `SECRET_KEY` is not supplied one will be generated.
