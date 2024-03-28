def heap_sort(arr,n,k):  
    global count
    count=0
    build_min_heap(arr,n,k)
    for idx in range (n,1,-1):
        
        temp=arr[1]
        arr[1]=arr[idx]
        arr[idx]=temp
        
        count=count+1
        if k==count:
            print(arr[idx] , arr[1])
            print(arr)
            
        heapify(arr,1,idx-1,k)
    
    if k>count:
        print(-1)
    

def build_min_heap(arr,n,k):
    for idx in range (int(n/2),0,-1):
        heapify(arr,idx,n,k)
        
def heapify(arr,k,n,limit):
    left=2*k
    right=2*k+1
    global count
    
    if right<=n:
        if arr[left]<arr[right]:
            smaller=left
        else:
            smaller=right    
    elif left<=n:
        smaller=left
    else:
        return
    if arr[smaller] < arr[k] :
        
        temp=arr[smaller]
        arr[smaller]=arr[k]
        arr[k]=temp
        
        count=count+1
        if limit==count:
            print(arr[k] , arr[smaller])
            print(arr)
        heapify(arr,smaller,n,limit)

def main():  
    
    N,k=map(int,input().split())
    arr=list(map(int,input().split()))
    
    heap_sort(arr,N,k)
    
if __name__=="__main__":
    main()