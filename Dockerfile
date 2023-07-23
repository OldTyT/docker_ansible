FROM python:3.10.6-slim-bullseye

ENV TYPE="diff" \
    ANSIBLE_HOST_KEY_CHECKING="False"

COPY entrypoint.sh /entrypoint.sh

RUN apt update && \
    apt install -y ssh && \
    python3 -m pip --no-cache-dir install ansible-core==2.15.2 ansible-compat==4.1.5 testinfra==6.0.0 && \
    rm -rf /var/lib/apt/lists/* && \
    mkdir /root/.ssh

ENTRYPOINT ['/entrypoint.sh']
