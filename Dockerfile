# Base image
FROM python:3-alpine

# Information
LABEL maintainer="FrozenFOXX <frozenfoxx@churchoffoxx.net>"

# Variables
WORKDIR /app
ENV APPDIR="/app" \
  APP_DEPS="ffmpeg"

# Install package dependencies
RUN apk -U add ${APP_DEPS}

# Install Python dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy app source
COPY . .

# Launch
ENTRYPOINT [ "/app/scripts/entrypoint.sh" ]
