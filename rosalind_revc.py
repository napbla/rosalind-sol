def find_complement(nucl):
	if nucl=="A":
		return "T"
	if nucl=="T":
		return "A"
	if nucl=="C":
		return "G"
	if nucl=="G":
		return "C"


def dna_complement(string_nucl):
	return "".join(filter(None,map(find_complement,string_nucl)))

with open('rosalind_revc.txt','r') as f:
    input_string = f.read()

with open('rosalind_revc_out.txt','w') as g:
    g.write(dna_complement(input_string)[::-1])
