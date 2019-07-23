import glob

glob.glob('igm/projects/Water_Contamination/input', '*.gz')
glob.glob('igm/projects/Water_Contamination/output/matching_output')
glob.glob('igm/projetcs/Water_Contamination/output/nonmatching_output')
glob.glob('igm/projects/Water_Contamination/references')
glob.glob('igm/projects/Water_Contamination/stats', '*.txt')

def build_command(args):

    input=glob(args.input)

    matching_output=glob(args.matching_output)

    nonmatching_output=glob(args.nonmatching_output)

    stats=glob(args.stats)

    references=glob(args.references)
