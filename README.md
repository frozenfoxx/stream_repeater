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

# Configuration

At this time a configuration file is required. A sample is provided in [./conf/stream_repeater.yaml](the conf directory). The fields are as such:

* `accounts`: all account information for services you wish to use. If you do not with to use or do not have appropriate credentials for a service, simply omit them. All supported services and their required credentials are listed in the sample file.
* `system`: all system configuration goes here and should not require modification unless you know what you're doing.
* `stream`: all configuration for the stream to handle.
  * `album`: the album description.
  * `bitrate`: desired MP3 bitrate.
  * `cover`: cover image, will be resized if necessary for each service.
  * `cuesheet`: (optional) CUE file with time codes and track listing.
  * `historysheet`: (optional) history file with time codes and track listing.
  * `mp3file`: (optional) name of the MP3 file. If it exists, it will not be overwritten. If no name provided, one will be generated.
  * `performer`: name of the performer.
  * `sourcefile`: name of the file to use for conversion (WAV only at this time).
  * `tags`: array of tags to apply.
  * `title`: title of the stream.

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

# Licenses

This software is provided under the Apache License, with the [https://startbootstrap.com/template/simple-sidebar]('Simple Sidebar Bootstrap theme') covered by the MIT license.
