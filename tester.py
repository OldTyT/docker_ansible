import os
import yaml

separator = "=" * 70


def get_hosts() -> list:
    with open('inventory.yml', 'r') as file:
        inventory = yaml.safe_load(file)
        hosts_list = []
        for children in inventory['all']['children']:
            for hosts in inventory['all']['children'][children]['hosts']:
                hosts_list.append(hosts)
        return hosts_list


def get_tests_cmd(hosts: list) -> list:
    cmd_list = []
    for host in hosts:
        cmd_list.append(f"test -f testinfra_{host}.py && printf '\033[0;32m\n{separator}\nTesting: {host}\n{separator}\n\033[0m\n' && py.test -v --color=yes --hosts={host} --ansible-inventory=inventory.yml --connection=ansible  testinfra_{host}.py || printf '\033[0;33m\n{separator}\nWarning!\nNot found test for: {host}\n{separator}\033[0m\n'")
    if os.getenv("WORKER_NODES_LIST") is not None:
        cmd_list.append(f"test -f testinfra_worker.py && printf '\033[0;32m\n{separator}\nTesting: worker\n{separator}\n\033[0m\n' && py.test -v --color=yes --hosts={os.getenv('WORKER_NODES_LIST')} --ansible-inventory=inventory.yml --connection=ansible  testinfra_worker.py || printf '\033[0;33m\n{separator}\nWarning!\nNot found test for: worker\n{separator}\033[0m\n'")
    if os.getenv("MASTER_NODES_LIST") is not None:
        cmd_list.append(f"test -f testinfra_master.py && printf '\033[0;32m\n{separator}\nTesting: master\n{separator}\n\033[0m\n' && py.test -v --color=yes --hosts={os.getenv('MASTER_NODES_LIST')} --ansible-inventory=inventory.yml --connection=ansible  testinfra_master.py || printf '\033[0;33m\n{separator}\nWarning!\nNot found test for: master\n{separator}\033[0m\n'")
    if os.getenv("TEST_ALL_DISABLED") != "True":
        cmd_list.append(f"printf '\033[0;32m\n{separator}\nTesting: all\n{separator}\n\033[0m\n' && py.test -v --color=yes --hosts=all --ansible-inventory=inventory.yml --connection=ansible  testinfra_all.py")
    return cmd_list


def return_cmds(cmds: list):
    for cmd in cmds:
        print(cmd)
    return


def main():
    hosts = get_hosts()
    cmds = get_tests_cmd(hosts)
    return_cmds(cmds)


if __name__ == '__main__':
    main()
