from paramiko import SSHClient, AutoAddPolicy, Channel


class SSHPackage:
    def __init__(self, hostname: str, username: str, password: str, port: int):
        self.hostname = hostname
        self.username = username
        self.password = password
        self.port = port

    def __enter__(self):
        class SSH:
            def __init__(self, hostname: str, username: str, password: str, port: int):
                self.ssh = SSHClient()
                self.ssh.set_missing_host_key_policy(AutoAddPolicy())
                self.ssh.connect(hostname=hostname, username=username, password=password, port=port)

            def execute(self, command: str) -> (Channel, Channel, Channel):
                return self.ssh.exec_command(command)

            def close(self):
                self.ssh.close()

        self.ssh_object = SSH(self.hostname, self.username, self.password, self.port)
        return self.ssh_object

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.ssh_object.close()