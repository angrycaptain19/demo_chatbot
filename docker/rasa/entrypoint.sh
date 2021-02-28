#!/bin/bash

echo " from rasa docker......."
service ssh start

set -Eeuo pipefail

function print_help {
    echo "Available options:"
    echo " help   - Print this help"
    echo " run    - Run an arbitrary command inside the container"
}

echo "new..."
echo "${1}"
echo "${@:1}"

case ${1} in
    run)
        exec python -m rasa "${@:1}"
        ;;
    train)
        exec python -m rasa train "${@:1}"
        ;;
    *)
        print_help
        ;;
esac