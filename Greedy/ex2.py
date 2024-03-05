N,M,K=map(int,input().split()) # input variables N:size of list M:total add count K: count which can add at once

num_list=list(map(int,input().split()))
ans=0
num_list.sort()
biggest=num_list[N-1]
sec_biggest=num_list[N-2]

times=M//(K+1)
others=M%(K+1)
count=K*times+others

ans=count*biggest
ans+=(M-count)*sec_biggest

print(ans)