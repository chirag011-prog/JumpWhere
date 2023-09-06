def kth_perm(n,k):
    permutation=[]
    unused = list(range(1,n+1))
    fact = [1]*(n+1)
    for i in range(1, n+1):
        fact[i] = i*fact[i-1]
    k-=1
    while n>0:
        part_leng = fact[n]//n
        i = k//part_leng
        permutation.append(unused[i])
        unused.pop(i)
        n -=1
        k %= part_leng
    return ''.join(map(str, permutation))
print(kth_perm(3,3))