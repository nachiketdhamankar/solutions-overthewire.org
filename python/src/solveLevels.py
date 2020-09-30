from python.src.ssh_wrapper import SSHPackage
import json
from pathlib import Path

bandit_hostname = "bandit.labs.overthewire.org"
max_level = 5


def main_runner(solution_dict):
    password = "bandit0"
    for level in range(0, max_level):
        with SSHPackage(hostname=bandit_hostname, username=f"bandit{level}", password=password,
                        port=2220) as s:
            for command in solution_dict[f"l{level}"]:
                print(f"Solving level: {level}")
                (stdin, stdout, stderr) = s.execute(command)
                password = stdout.read().decode('ascii').strip('\n')
                print(f"At level {level}, password: {password}")


if __name__ == '__main__':
    solutions_file = Path.cwd().parent.parent / f"solutions.json"
    with open(solutions_file, 'r') as solutions:
        solutions_dict = json.load(solutions)
        main_runner(solutions_dict)
