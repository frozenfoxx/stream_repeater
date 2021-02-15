#!/usr/bin/env ash

# If the SECRET_KEY isn't set, generate one
if [[ -z ${SECRET_KEY} ]]; then
  SECRET_KEY=$(python -c 'import os; print(os.urandom(24))')
fi

pip3 install .
flask run