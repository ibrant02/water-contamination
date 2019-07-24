QSUB_ARGUMENTS = ['N', 'cwd', 'pe', 'q', 'S', 'V', 'j', 'b', 'Xmx']


def build_command(args, command):
    """Build the qsub command.

    Args:
        args: The arguments to this qsub command
        command (str): The command to run on a Torque scheduler

    Return:
        the str qsub command that was built
    """
    string_list = ["qsub"]
    for arg in dir(args):
        if arg.startswith("_") or arg not in QSUB_ARGUMENTS:
            continue
        arg_value = getattr(args, arg)
        if not arg.startswith('X'):
            if not arg_value == "true":
                string_list.append("-{} {}".format(arg, arg_value))
            else:
                string_list.append("-{}".format(arg))
        else:
            string_list.append("--{} {}".format(arg, arg_value))
    string_list.append(command)
    return " ".join(string_list)
