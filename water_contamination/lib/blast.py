from Bio.Blast import NCBIWWW, NCBIXML


def get_blast_results(fasta_filename, blast_type="blastn", db="nt"):
    """Get the results from NCIB BLAST for the given FASTA file.

    Args:
        fasta_filename (str): The path to the FASTA file to run against BLAST
        blast_type (str): The type of BLAST to run ("blastn", "blastp", etc.)
        db (str): The blast database to run this query against ("nt", "pt", etc.)

    Return:
        list of Bio.Blast.Record.Blast records
    """
    fasta_sequence = None
    with open(fasta_filename, 'r') as fasta_file:
        fasta_sequence = fasta_file.read()

    results = NCBIWWW.qblast(blast_type, db, fasta_sequence)
    blast_records = NCBIXML.parse(results)
    return list(blast_records)
