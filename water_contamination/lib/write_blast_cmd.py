#!/usr/bin/env python


# tab-delimited file with all the possible options
# see "blastn -help"
DEFAULT_OUTPUT_FORMAT = (
    '\'6 qseqid qgi qacc qaccver qlen sseqid sallseqid sgi sallgi sacc '
    'saccver sallacc slen qstart qend sstart send qseq sseq evalue bitscore '
    'score length pident nident mismatch positive gapopen gaps ppos frames '
    'qframe sframe btop staxid ssciname scomname sblastname sskingdom staxids '
    'sscinames scomnames sblastnames sskingdoms stitle salltitles sstrand '
    'qcovs qcovhsp qcovus\''
)


def build_type(n_or_x):
    if n_or_x is None:
        n_or_x = "n"

    if n_or_x == "n":
        db = "-db nt"
    elif n_or_x == "x":
        db = "-db nr"

    return "blast{}".format(n_or_x) + " " + db


def build_max_target_seqs(max_targets):
    if max_targets is None:
        max_targets = 1
    return "-max_target_seqs {}".format(max_targets)


def build_threads(threads):
    if threads is None:
        threads = 1
    return "-num_threads {}".format(threads)


def build_out_file(blast_stats_out):
    if blast_stats_out is None:
        blast_stats_out = "blast_report.txt"
    return "-out {}".format(blast_stats_out)


def build_query_input(fasta_input):
    return "-query {}".format(fasta_input)


def build_output_format(output_format):
    if output_format is None:
        output_format = DEFAULT_OUTPUT_FORMAT
    return "-outfmt {}".format(output_format)


def build_blast_command(args):
    """Builds an executable BLAST command

    Args:
        Required: fasta_input
    Return:
        String of the form 'blastn -max_target_seq ...
    """
    command_list = []

    command_list.append(build_type(args.n_or_x))
    command_list.append(build_max_target_seqs(args.max_targets))
    command_list.append(build_threads(args.threads))
    command_list.append(build_out_file(args.blast_stats_out))
    command_list.append(build_query_input(args.fasta_input))
    command_list.append(build_output_format(args.output_format))

    print(" ".join(command_list))
    return " ".join(command_list)


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--blast-type", "-b", dest="n_or_x",
                        help="Specify blastn or blastx", choices=['n', 'x'],
                        default="n")
    parser.add_argument("--max-targets", "-m", type=int, default=1,
                        help="How many hits blast may return. Default is 1.")
    parser.add_argument("--threads", "-t", type=int, default=1,
                        help="How many threads with which to run BLAST.")
    parser.add_argument("--blast-stats-out", "-o", default="blast_report.txt",
                        help="Name of file to which blast will write results")
    parser.add_argument("--fasta-input", "-f", required=True,
                        help="FASTA reads to identify")
    parser.add_argument("--output-format",
                        help="See blastn -help for -outfmt choices")
    args = parser.parse_args()
    build_blast_command(args)
