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

To load the application launch the container with your configuration:

```
docker run \
  -it \
  --rm \
  -v [mount point]:/data \
  -p 5000:5000 \
  frozenfoxx/stream_repeater:latest \
    -c /data/stream_repeater.yaml
```

Then access [http://localhost:5000](http://localhost:5000).