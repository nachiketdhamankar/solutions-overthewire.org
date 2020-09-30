from python.ssh_wrapper import SSHPackage
import json
from pathlib import Path

bandit_hostname = "bandit.labs.overthewire.org"
max_level = 4


def level4(password_level3: str) -> str:
    with SSHPackage(hostname=bandit_hostname, username="bandit4", password=password_level3,
                    port=2220) as s:
        (stdin, stdout, stderr) = s.execute(f"ls inhere")

        list_file_str = stdout.read().decode('ascii').strip('\n')
        files = list_file_str.split('\n')
        for file in files:
            (stdin, stdout, stderr) = s.execute(f"cat inhere/{file}")
            try:
                content = stdout.read().decode('ascii').strip('\n')
                print(content)
                return content
            except UnicodeDecodeError as e:
                continue


def main_runner(solution_dict):
    password = "bandit0"
    for level in range(0, max_level):
        for command in solution_dict[f"l{level}"]:
            with SSHPackage(hostname=bandit_hostname, username=f"bandit{level}", password=password,
                            port=2220) as s:
                print(f"Solving level: {level}")
                (stdin, stdout, stderr) = s.execute(command)
                password = stdout.read().decode('ascii').strip('\n')
                print(f"At level {level}, password: {password}")


if __name__ == '__main__':
    solutions_file = Path.cwd().parent / f"solutions.json"
    with open(solutions_file, 'r') as solutions:
        solutions_dict = json.load(solutions)
        main_runner(solutions_dict)
