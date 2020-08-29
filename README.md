# stream_repeater

Convert, upload, and post audio and video streams to remote services.

# Usage

## Docker

To load the interface interactively provide the following:

```
docker run \
  -it \
  --rm \
  -v [path to]/stream_repeater.yaml:/data/stream_repeater.yaml \
  frozenfoxx/stream_repeater:latest \
    -c /data/stream_repeater.yaml
```