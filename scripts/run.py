def main(*args, **kwargs):

    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=list, help="fastq1, fastq2 (Coma seperated)")
    parser.add_argument("--nonmatching_output", type=list, help="out1 and out2")
    parser.add_argument("--matching_output", type=list, help="outm1 and outm2")
    parser.add_argument("--reference", type=list, help="reference, reference (Coma seperated)")
    parser.add_argument("--stat", type=list, help="stat")
    parser.add_argument("--minavgquality", type=str, help="the minimum average quality.")
    parser.add_argument("--trimpolya", type=str, help="trimpolya")
    parser.add_argument("--minilength", type=str, help="mimimum length")
    parser.add_argument("--maxns", type=str, help="maxns")
    parser.add_argument("--k", type=str, help="k-mer")
    parser.add_argument("--t", type=str, help="t")
    parser.add_argument("--zl", type=str, help="zl")
    parser.add_argument("--ow", type=str, help="ow")
    parser.add_argument("--entropy", type=str, help="entropy")
    args=parser.parse_args()
    #answer=args.list("input", "output", "reference", "stats")
    #answer=args.str("minavgquality", "trimpolya", "minilength", "maxns", "k", "t", "zl", "entropy", "ow")
    print(args.input)
    print("Isaiah wrote a successful entrypoint script!")
