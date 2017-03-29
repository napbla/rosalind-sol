"""Ham so tong quat la F(n) = F(n-1)+ k*F(n-2) voi F(1)=F(2)=1 """

def modified_fibo(n,m):
    a = [1,1]
    i = 2
    while i<n:
        if (i<m+1):
            a.append(a[i-1]+a[i-2])
        else:
            a.append(a[i-1]+a[i-2]-a[i-m-1])
        print a
        i=i+1
    return a[n-1]


    
with open('rosalind_fibd.txt','r') as f:
    input_string = f.read()

with open('rosalind_fibd_out.txt','w') as g:
    n = int(input_string.split(" ")[0]);
    m = int(input_string.split(" ")[1]);
    g.write(str(modified_fibo(n,m)))
