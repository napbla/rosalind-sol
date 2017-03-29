def read_fasta(fp):
    name, seq = None, []
    for line in fp:
        line = line.rstrip()
        if line.startswith(">"):
            if name: yield (name, ''.join(seq))
            name, seq = line, []
        else:
            seq.append(line)
    if name: yield (name, ''.join(seq))

def calculate_percent(s):
    return (s.count("C")+s.count("G"))/float(len(s))

with open('rosalind_gc.txt','r')as fp:
    with open('rosalind_gc_out.txt','w')as out_put:    
        max_percent = 0.0
        max_seq = ""
        for name, seq in read_fasta(fp):
            temp = calculate_percent(seq)
            if temp>max_percent:
                max_percent = temp
                max_seq=name
        out_put.write(name[1:]+"\n")
        out_put.write("{0:0.6f}".format(max_percent*100))
