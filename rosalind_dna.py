def compare(s1,s2):
    if len(s1)==0:
        return 0
    else:
        if (s1[0] == s2[0]):
            return 0 + compare(s1[1:],s2[1:])
        else:
            return 1 + compare(s1[1:],s2[1:])
                
with open('rosalind_hamm.txt','r') as f:
    input_string = f.read()

with open('rosalind_hamm_out.txt','w') as g:
    first_dna = input_string.split("\n")[0]
    second_dna = input_string.split("\n")[1]
    g.write(str(compare(first_dna,second_dna)))
    
