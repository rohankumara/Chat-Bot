from pathlib import Path

import paramiko
from loguru import logger

# to suppress https://github.com/paramiko/paramiko/issues/1386
import warnings
warnings.filterwarnings(action='ignore',module='.*paramiko.*')


def get_current_user_home_dir():
    return str(Path.home())

class Session(object):
    host = None
    ssh_client = None

    def __init__(self, host):
        self.host = host
        self.ssh_client = paramiko.SSHClient()
        self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh_client.connect(self.host, username="root", key_filename="{}/.ssh/id_rsa.pub".format(get_current_user_home_dir()))

    @property
    def hosts(self):
        with open("/etc/hosts") as fp:
            env_hosts = [host.rstrip().replace("\t", " ") for host in fp.readlines() if not host.startswith("#")]
        return env_hosts

    def execute(self, command):
        std_in, stdout, stderr = self.ssh_client.exec_command(command)
        std_in.close()
        for output in iter(lambda: stdout.readline(2048), ""): yield output.rstrip()

    def close(self):
        self.ssh_client.close()
