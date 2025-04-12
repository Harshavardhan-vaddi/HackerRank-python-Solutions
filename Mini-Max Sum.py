def miniMaxSum(arr):
    n=len(arr)
    res1=0
    res2=0
    arr.sort()
    for i in range(n-1):
        res1+=arr[i]
    for i in range(1,n):
        res2+=arr[i]
    print(res1,res2)
    

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    miniMaxSum(arr)
