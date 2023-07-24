#!/bin/bash

echo "$SSH_KEY_PRIVATE"|base64 -d > /root/.ssh/id_rsa
chmod 600 /root/.ssh/id_rsa

if [ "$TYPE" = "diff" ]; then
    ansible-playbook --diff -i ./inventory.yml playbook.yml && exit
fi
if [ "$TYPE" = "test" ]; then
    py.test -v --color=yes --hosts=all --ansible-inventory=inventory.yml --connection=ansible  testinfra_all.py
fi
if [ "$TYPE" = "play" ]; then
    ansible-playbook -i ./inventory.yml playbook.yml && exit
else
    echo "Invalid env value - $TYPE"
    exit 1
fi
