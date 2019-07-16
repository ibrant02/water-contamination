from water_contamination.lib.bbduk import build_command


def main(*args, **kwargs):
    #import pdb; pdb.set_trace()
    import argparse

    parser=argparse.ArgumentParser()
    parser.add_argument("-input", type=list, help="fastq1, fastq2 (Coma seperated)")
    parser.add_argument("-nonmatching_output", type=list, help="out1 and out2")
    parser.add_argument("-matching_output", type=list, help="outm1 and outm2")
    parser.add_argument("-references", type=list, help="references, reference (Coma seperated)")
    parser.add_argument("-stats", type=list, help="stats")
    parser.add_argument("-minavgquality", type=int, default=5, help="choose a minavgquality value or stay with the default of 5")
    parser.add_argument("-trimpolya", type=int, default=7, help="choose a trimpolya value or stay with the default of 7")
    parser.add_argument("-minilength", type=int, default=51, help="choose a minilength value or stay with the default of 51")
    parser.add_argument("-maxns", type=int, default=1, help="choose a maxns value or stay with the default of 1")
    parser.add_argument("-k", type=int, default=25, help="choose a k value or stay with the default of 25")
    parser.add_argument("-t", type=int, default=2, help="choose a t value or stay with the default of 2")
    parser.add_argument("-zl", type=int, default=6, help="choose zl value or stay with the default of 6")
    parser.add_argument("-entropy", type=float, default=0.5, help="choose an entropy value or stay with the default of 0.5")
    parser.add_argument("-ow", type=str, default="t", help="choose an ow value or stay with the default of t")
    args=parser.parse_args()
    
    bbduk_command=build_command(args)
    if args.minavgquality:
        print("minavgquality={}".format(args.minavgquality))
    if args.trimpolya:
        print("trimpolya={}".format(args.trimpolya))
    if args.minilength:
        print("minilength={}".format(args.minilength))
    if args.maxns:
        print("maxns={}".format(args.maxns))
        print(type(args.maxns))
    if args.k:
        print("k={}".format(args.k))
    if args.t:
        print("t={}".format(args.t))
    if args.zl:
        print("zl={}".format(args.zl))
    if args.entropy:
        print("entropy={}".format(args.entropy))
    if args.ow:
        print("ow={}".format(args.ow))
