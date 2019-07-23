from water_contamination.lib.bbduk import build_command

def main(*args, **kwargs):
    #import pdb; pdb.set_trace()
    import argparse

    parser=argparse.ArgumentParser()
    parser.add_argument("-input", type=str, help="fastq1, fastq2 (Coma seperated)")
    parser.add_argument("--nonmatching_output", "-out", type=str, help="out1 and out2")
    parser.add_argument("--matching_output", "-outm", type=str, help="outm1 and outm2")
    parser.add_argument("-references", type=str help="references, reference (Coma seperated)")
    parser.add_argument("-stats", type=list, help="stats")
    parser.add_argument("-minavgquality", type=int, default=5, help="choose a minavgquality value or stay with the default of 5")
    parser.add_argument("-trimpolya", type=int, default=7, help="choose a trimpolya value or stay with the default of 7")
    parser.add_argument("-minlength", type=int, default=51, help="choose a minlength value or stay with the default of 51")
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
        print("minlength={}".format(args.minlength))
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

def build_input(fastq1, fastq2):
    return "in1=" + fastq1 + " in2=" + fastq2

def build_nonmatching_output(fastq1, fastq2):
    return "out1=" + fastq1 + " out2=" + fastq2

def build_matching_output(fastq1, fastq2):
    return "outm1=" + fastq1 + " outm2=" + fastq2

def build_reference(references):
    return "ref=" + ",".join(references)

def build_stats(stats):
    return "stats=" + stats

def build_minavgquality(minavgquality=5):
    return "minavgquality={}".format(minavgquality)

def build_trimpolya(trimpolya=7):
    return "trimpolya={}".format(trimpolya)

def build_minlength(minilength=51):
    return "minlength={}".format(minlength)

def build_maxns(maxns=1):
    return "maxns={}".format(maxns)

def build_k(k=25):
    return "k={}".format(k)

def build_t(t=2):
    return "t={}".format(t)

def build_zl(zl=6):
    return "zl={}".format(zl)

def build_entropy(entropy=0.5):
   return "entropy={}".format(entropy)

def build_ow(ow="T"):
    return "ow={}".format(ow)

def build_command(args):

    string_list=[]
    string_list.append(igm//apps/bbmap/bbmap/bbduk.sh)

    print(args.input)
    fastq1, fastq2=args.input.split(",")
    input=build_input(args.input)
    string_list.append(input)

    print(args.matching_output)
    fastq1, fastq2=args.matching_output(",")
    matching_output=build_matching_output(args.matching_output)
    string_list.append(matching_output)

    print(args.nonmatching_output)
    fastq1, fastq2=args.nonmatching_output(",")
    nonmatching_output=build_nonmatching_output(args.nonmatching_output)
    string_list.appending(nonmatching_output)

    stats=build_stats(args.stats)
    string_list.appending(stats)

    references=build_references(args.references)
    string_list.append(references)

    trimpolya=build_trimpolya(args.trimpolya)
    string_list.append(trimpolya)

    minlength=build_minlength(args.minlength)
    string_list.append(minlength)

    maxns=build_mans(args.maxns)
    string_list.append(maxns)

    minavgquality=build_minavgquality(args.minavgquality)
    string_list.append(minavgquality)

    k=build_k(args.k)
    string_list.append(k)

    t=build_t(args.t)
    string_list.append(t)

    zl=build_zl(args.zl)
    string_list.append(zl)

    ow=build_ow(args.ow)
    string_list.append(ow)

    entropy=build_entropy(args.entropy)
    string_list.append(entropy)
