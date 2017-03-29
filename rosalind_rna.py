def dna_to_rna(s):
	return s.replace("T","U")
    
with open('rosalind_rna.txt','r') as f:
    input_string = f.read()

with open('rosalind_rna_out.txt','w') as g:
    g.write(dna_to_rna(input_string))
    
