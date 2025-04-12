def plusMinus(arr):
    n=len(arr)
    l,z,g=0,0,0
    for i in range(n):
        if arr[i]<0:
            l+=1
        if arr[i]==0:
            z+=1
        if arr[i]>0:
            g+=1
    print("%.6f"%(g/n))
    print("%.6f"%(l/n))
    print("%.6f"%(z/n))
    
if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    plusMinus(arr)
