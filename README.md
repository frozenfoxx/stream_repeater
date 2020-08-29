# stream_repeater

Convert, upload, and post audio and video streams to remote services.

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

To load the interface interactively provide the following:

```
docker run \
  -it \
  --rm \
  -v [mount point]:/data \
  frozenfoxx/stream_repeater:latest \
    -c /data/stream_repeater.yaml
```

To run in batchmode:

```
To load the interface interactively provide the following:

```
docker run \
  -it \
  --rm \
  -v [mount point]:/data \
  frozenfoxx/stream_repeater:latest \
    -b \
    -c /data/stream_repeater.yaml
```