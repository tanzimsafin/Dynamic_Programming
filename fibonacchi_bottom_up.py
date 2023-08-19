array=[]
array.append(0)
array.append(1)
def fibo_bottom_up(n):
    for i in range(1,n):
        array.append(array[i]+array[i-1])
    return array[n]
print(fibo_bottom_up(10))
print(array)