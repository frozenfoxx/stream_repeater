#!/usr/bin/env ash

# Variables
APPDIR=${APPDIR:-"/app"}

# Functions

# Logic

python ${APPDIR}/stream_repeater/stream_repeater.py $@
