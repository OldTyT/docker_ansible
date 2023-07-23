#!/bin/bash

echo "$SSH_PRIVATE_KEY"|base64 -d > /root/.ssh/id_rsa

if [ "$TYPE" = "diff" ]; then
    ansible-playbook --diff -i ./inventory.yml playbook.yml && exit
fi
if [ "$TYPE" = "play" ]; then
    ansible-playbook -i ./inventory.yml playbook.yml && exit
else
    echo "Invalid env value - $TYPE"
    exit 1
fi