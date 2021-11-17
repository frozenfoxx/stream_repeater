# Base image
FROM python:3-alpine

# Information
LABEL maintainer="FrozenFOXX <frozenfoxx@churchoffoxx.net>"

# Variables
WORKDIR /app
ENV APPDIR="/app" \
  APP_DEPS="ffmpeg imagemagick" \
  BUILD_DEPS="build-base libffi-dev openssl-dev python3-dev" \
  CONFIG="/etc/stream_repeater/conf/stream_repeater.yaml" \
  FLASK_APP="stream_repeater" \
  FLASK_ENV="development" \
  FLASK_RUN_HOST="0.0.0.0" \
  FLASK_RUN_PORT="5000" \
  SECRET_KEY=''

# Install package dependencies
RUN apk -U add ${APP_DEPS} ${BUILD_DEPS}

# Install Python dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy app source
COPY . .

# Clean up 
RUN apk del ${BUILD_DEPS}

# Expose listen port
EXPOSE 5000

# Launch
ENTRYPOINT [ "./scripts/entrypoint.sh" ]
