"""Ham so tong quat la F(n) = F(n-1)+ k*F(n-2) voi F(1)=F(2)=1 """

def modified_fibo(n,k):
    if n==1 or n==2:
        return 1
    else:
        return modified_fibo(n-1,k) + k*modified_fibo(n-2,k)

with open('rosalind_fib.txt','r') as f:
    input_string = f.read()

with open('rosalind_fib_out.txt','w') as g:
    n = int(input_string.split(" ")[0]);
    k = int(input_string.split(" ")[1]);
    g.write(str(modified_fibo(n,k)))
