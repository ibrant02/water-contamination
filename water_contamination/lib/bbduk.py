def build_input(fastq1, fastq2):
    return "in1=" + fastq1 +  " in2=" + fastq2

def build_nonmatching_output(out1, out2):
    return "out1=" + out1  +  " out2=" + out2

def build_matching_output(outm1, outm2):
    return "outm1=" + outm1 +  " outm2=" + outm2

def build_references(references):
    return "ref=" + references

def build_stats(stats):
    return "stats=" + stats

def build_minavgquality(minavgquality=5):
    return "minavgquality={}".format(minavgquality)

def build_trimpolya(trimpolya=7):
    return "trimpolya={}".format(trimpolya)

def build_minlength(minlength=51):
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

#def build_Xmx(Xmx=200):
#    return "Xmx={}g".format(Xmx)

def build_ow(ow="T"):
    return "ow={}".format(ow)

def build_command(args):

    string_list=[]
    string_list.append("/igm//apps/bbmap/bbmap/bbduk.sh")

    print(args.input)
    fastq1, fastq2=args.input.split(",")
    input=build_input(fastq1, fastq2)
    string_list.append(input)

    print(args.matching_output)
    out1, out2=args.matching_output.split(",")
    matching_output=build_matching_output(out1, out2)
    string_list.append(matching_output)

    print(args.nonmatching_output)
    outm1, outm2=args.nonmatching_output.split(",")
    nonmatching_output=build_nonmatching_output(outm1, outm2)
    string_list.append(nonmatching_output)

    print(args.stats)
    stats=build_stats(args.stats)
    string_list.append(stats)

    print(args.references)
    references=build_references(args.references)
    string_list.append(references)
    references.split(",")

    trimpolya=build_trimpolya(args.trimpolya)
    string_list.append(trimpolya)

    minlength=build_minlength(args.minlength)
    string_list.append(minlength)

    maxns=build_maxns(args.maxns)
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

    #Xmx=build_Xmx(200)
    #string_list.append(Xmx)
