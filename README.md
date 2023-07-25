# docker_ansible

Docker image for play ansible playbooks in pipeline and testing with testinfra

## Environment variable

|ENV|Default value|What does it do?|
|---|---|---|
|`TYPE`|`diff`|Type launch(diff, play or test)|
|`SSH_KEY_PRIVATE`|`""`|SSH private key encrypted with base64|
|`TEST_ALL_DISABLED`|`""`|Disabled all tests if setup `True`|
|`WORKER_NODES_LIST`|`""`|Launch test for node worker, ex: `host1,host2`|
|`MASTER_NODES_LIST`|`""`|Launch test for node master, ex: `host1,host2`|

## Example Gitlab CI

```yaml
---
stages:
  - ansible_diff
  - ansible_play
  - ansible_test

ansible_diff:
  stage: ansible_diff
  image: ghcr.io/oldtyt/docker_ansible
  script: [/entrypoint.sh]

ansible_play:
  needs: [ansible_diff]
  variables:
    TYPE: "play"
  stage: ansible_play
  image: ghcr.io/oldtyt/docker_ansible
  script: [/entrypoint.sh]
  only: [main]
  when: manual

ansible_test:
  needs: [ansible_play]
  variables:
    TYPE: "test"
  stage: ansible_test
  image: ghcr.io/oldtyt/docker_ansible
  only: [main]
  script: [/entrypoint.sh]
```