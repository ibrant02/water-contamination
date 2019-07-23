import argparse

parser=argparse.ArgumentParser()
parser.add_argument("-minavgquality", type=int, help="choose one of the following bbduk variables:[minavgquality, trimpolya, minlength, maxns, k, t, zl, entropy, ow]")
parser.add_argument("-trimpolya", type=int, help="choose one of the following bbduk variables:[minavgquality, trimpolya, minlength, maxns, k, t, zl, entropy, ow]")
parser.add_argument("-minlength", type=int, help="choose one of the following bbduk variables:[minavgquality, trimpolya, minlength, maxns, k, t, zl, entropy, ow]")
parser.add_argument("-maxns", type=int, help="choose one of the following bbduk variables:[minavgquality, trimpolya, minlength, maxns, k, t, zl, entropy, ow]")
parser.add_argument("-k", type=int, help="choose one of the following bbduk variables:[minavgquality, trimpolya, minlength, maxns, k, t, zl, entropy, ow]")
parser.add_argument("-t", type=int, help="choose one of the following bbduk variables:[minavgquality, trimpolya, minlength, maxns, k, t, zl, entropy, ow]")
parser.add_argument("-zl", type=int, help="choose one of the following bbduk variables:[minavgquality, trimpolya, minlength, maxns, k, t, zl, entropy, ow]")
parser.add_argument("-entropy", type=float, help="choose one of the following bbduk variables:[minavgquality, trimpolya, minlength, maxns, k, t, zl, entropy, ow]")
parser.add_argument("-ow", type=str, help="choose one of the following bbduk variables:[minavgquality, trimpolya, minlength, maxns, k, t, zl, entropy, ow]")
args=parser.parse_args()
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
