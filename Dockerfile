FROM python:3.10.6-slim-bullseye

ENV TYPE="diff" \
    ANSIBLE_HOST_KEY_CHECKING="False"

COPY entrypoint.sh /usr/local/bin/
COPY tester.py /tester.py

RUN apt update && \
    apt install -y openssh-client rsync git && \
    python3 -m pip --no-cache-dir install ansible-core==2.15.2 ansible-compat==4.1.5 testinfra==6.0.0 ansible-lint==6.18.0 && \
    rm -rf /var/lib/apt/lists/* && \
    mkdir /root/.ssh && \
    ansible-galaxy collection install community.general community.docker ansible.posix kubernetes.core community.kubernetes

COPY ssh_config /etc/ssh/

ENTRYPOINT ["entrypoint.sh"]
