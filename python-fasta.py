
import sys

def read_fasta(filename):
    """reads fasta file and returns the sequence"""
    seq = ''
    f = open(filename)
    for line in f:
        line = line.strip() 
        if not '>' in line:
            seq = seq + line 
    f.close()
    return seq

if len(sys.argv) < 2:
    print ("Need to privide filename")
    exit(1)

print(read_fasta(sys.argv[1]))
