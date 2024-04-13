# 두 수의 합
# N,M=map(int,input().split())
# A=list(map(int,input().split()))
# start=0
# end=1
# count=0
# sum=A[0]
# while True:
#     if sum<M:
#         if end<N:
#             sum+=A[end]
#             end+=1
#         else:
#             break
#     elif sum==M:
#         count+=1
#         sum-=A[start]
#         start+=1
#     else:
#         sum-=A[start]
#         start+=1
# print(count)

# 수 고르기
import sys
input=sys.stdin.readline
N, M = map(int, input().split())

a = [int(input()) for _ in range(N)]
    
a.sort()
start=0
end=0
answer=2000000000

while end<N:
    diff=a[end]-a[start]
    if M > diff:
        end+=1
    elif diff>M:
        answer=min(diff,answer)
        start+=1
    else:
        answer=M
        break

print(answer)
