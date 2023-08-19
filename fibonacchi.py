memo={}
def fibo(n):
    if n in memo:
      return memo[n]
    if n==1 or n==0:
        return n
    f=fibo(n-1)+fibo(n-2)
    memo[n]=f
    return memo[n]
print(fibo(10))
print(memo)
    
    