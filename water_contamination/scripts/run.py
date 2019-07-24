import argparse
from configparser import ConfigParser

import water_contamination.lib.bbduk as bbduk
from water_contamination.lib.command import execute_command
import water_contamination.lib.qsub as qsub


def parse_config(config_path):
    """Parse the config file and check which arguments are provided.

    Args:
        config_path (str): The path to the config file

    Return:
        argparse.Namespace containing all of the arguments provided in the config
    """
    config = ConfigParser()
    config.read(config_path)
    sections = config.sections()
    config_values = argparse.Namespace()
    title_cased = ['n', 'xmx', 's', 'v']
    for section in sections:
        for option in config[section]:
            if option in title_cased:
                option = option.title()
            setattr(config_values, option, config[section][option.lower()])
    return config_values


def validate_arguments(args):
    """Validate that the arguments are acceptable for the program.

    Args:
        args (argparse.Namespace): The parsed arguments from the CLI

    Return:
        empty list if the arguments are valid, list of str if they aren't
    """
    errors = []
    if not args.config:
        required_args = ['input', 'nonmatching_output', 'matching_output', 'references', 'stats',
                         'N']
        for required in required_args:
            if not getattr(args, required):
                errors.append("The {} argument is required if a config file is not specified")
    return errors


def main(*args, **kwargs):
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=str, help="Path to a config file (.ini) with argument values. If provided, other command line args will be ignored.")

    bbduk_group = parser.add_argument_group('bbduk arguments')
    bbduk_group.add_argument("--input", type=str, help="fastq1, fastq2 (Comma seperated)")
    bbduk_group.add_argument("--nonmatching_output", "-out", type=str, help="out1 and out2")
    bbduk_group.add_argument("--matching_output", "-outm", type=str, help="outm1 and outm2")
    bbduk_group.add_argument("--references", "-ref", type=str, help="references, reference (Comma seperated)")
    bbduk_group.add_argument("--stats", type=str, help="stats")
    bbduk_group.add_argument("--minavgquality", type=int, default=5, help="choose a minavgquality value or stay with the default of 5")
    bbduk_group.add_argument("--trimpolya", type=int, default=7, help="choose a trimpolya value or stay with the default of 7")
    bbduk_group.add_argument("--minlength", type=int, default=51, help="choose a minlength value or stay with the default of 51")
    bbduk_group.add_argument("--maxns", type=int, default=1, help="choose a maxns value or stay with the default of 1")
    bbduk_group.add_argument("--k", type=int, default=25, help="choose a k value or stay with the default of 25")
    bbduk_group.add_argument("--t", type=int, default=2, help="choose a t value or stay with the default of 2")
    bbduk_group.add_argument("--zl", type=int, default=6, help="choose zl value or stay with the default of 6")
    bbduk_group.add_argument("--entropy", type=float, default=0.5, help="choose an entropy value or stay with the default of 0.5")
    bbduk_group.add_argument("--ow", type=str, default="t", help="choose an ow value or stay with the default of t")

    qsub_group = parser.add_argument_group('qsub arguments')
    qsub_group.add_argument("-N", type=str, help="The name of this job in Torque")
    qsub_group.add_argument("-cwd", action="store_true", help="If specified, execute the command from the current working directory")
    qsub_group.add_argument("-pe", type=str, help="Define the parallel environment this should execute in")
    qsub_group.add_argument("-q", type=str, default="all.q", help="Which queue this should be submitted to")
    qsub_group.add_argument("-S", type=str, default="/bin/bash", help="The interpreting shell for the job")
    qsub_group.add_argument("-V", action="store_true", help="All environment variables should be exported into the context of the job")
    qsub_group.add_argument("-j", type=str, default="y", help="Should stderr be merged into stdout?")
    qsub_group.add_argument("-b", type=str, default="y", help="Should command be treated as a binary file or script?")
    qsub_group.add_argument("--Xmx", type=str, default="200g", help="How much memory should be allocated to this qsub task")

    args = parser.parse_args()
    errors = validate_arguments(args)
    if errors:
        print("Encountered the following errors:")
        for error in errors:
            print(error)
        return

    if args.config:
        args = parse_config(args.config)

    bbduk_command = bbduk.build_command(args)
    qsub_command = qsub.build_command(args, bbduk_command)

    # Run the qsub command
    output, error = execute_command(qsub_command)
