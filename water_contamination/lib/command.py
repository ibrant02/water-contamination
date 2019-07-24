import shlex
import subprocess


def execute_command(command):
    """Executes the given command.

    Args:
        command (str): The command to execute

    Return:
        (stdout, stderr) from running the command
    """
    args = shlex.split(command)
    process = subprocess.Popen(args, stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    return process.stdout, process.stderr
