# Base image
FROM python:3-alpine

# Information
LABEL maintainer="FrozenFOXX <frozenfoxx@churchoffoxx.net>"

# Variables
WORKDIR /app
ENV APPDIR="/app" \
  APP_DEPS="ffmpeg imagemagick" \
  BUILD_DEPS="build-base libffi-dev python3-dev" \
  CONFIG="/etc/stream_repeater/conf/stream_repeater.yaml" \
  FLASK_APP="stream_repeater" \
  FLASK_ENV="development" \
  FLASK_RUN_HOST="0.0.0.0" \
  FLASK_RUN_PORT="5000" \
  MAGICK_HOME=/usr \
  SECRET_KEY=''

# Install package dependencies
RUN apk -U add ${APP_DEPS} ${BUILD_DEPS}

# Add symlinks for Wand, https://docs.wand-py.org/en/0.6.7/guide/install.html#install-wand-on-alpine
RUN ln -s /usr/lib/libMagickCore-7.Q16HDRI.so.9 /usr/lib/libMagickCore-7.Q16HDRI.so && \
  ln -s /usr/lib/libMagickWand-7.Q16HDRI.so.9 /usr/lib/libMagickWand-7.Q16HDRI.so

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
