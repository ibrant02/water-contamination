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

def bulid_minavgquality(minavgquality=5):
    return "minavgquality={}".format(minavgquality)

def build_trimpolya(trimpolya=7):
    return "trimpolya={}".format(trimpolya) 

def build_minilength(minilength=51):
    return "minilength={}".format(minilength)

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

    string_list=[input, output, reference, stats, minavgquality, trimpolya, minilength, maxns, k, t, zl, entropy, Xmx, ow]
    string_list.append("echo '{}'".format(igm//apps/bbmap/bbmap/bbduk.sh))

    input=build_input(args.input)
    string_list.append(input)

    
    matching_output=build_matching_output(args.matching_output)
    string_list.append(matching_output)

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

    #Xmx=build_Xmx(200)
    #string_list.append(Xmx)    
