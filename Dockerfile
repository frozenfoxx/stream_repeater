# Base image
FROM python:3-alpine

# Information
LABEL maintainer="FrozenFOXX <frozenfoxx@churchoffoxx.net>"

# Variables
WORKDIR /app
ENV APPDIR="/app" \
  APP_DEPS="build-base libffi-dev openssl-dev python3-dev" \
  FLASK_APP="stream_repeater" \
  FLASK_ENV="development"

# Install package dependencies
RUN apk -U add ${APP_DEPS}

# Install Python dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy app source
COPY . .

# Expose listen port
EXPOSE 5000

# Launch
ENTRYPOINT [ "./scripts/entrypoint.sh" ]
