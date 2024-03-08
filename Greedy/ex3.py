# # my answer
# N,M=map(int,input().split())

# cards=[list(map(int,input().split()))for _ in range(N)]


# for idx in range(N):
#     cards[idx].sort()

# max_ini=-1
# for idx in range(N):
#     if cards[idx][0]>=max_ini:
#         max_ini=cards[idx][0]

# print(max_ini)


# min() function
# N,M=map(int,input().split())
# result=-1
# for idx in range(N):
#     cards= list(map(int,input().split()))
#     min_value=min(cards)
#     result=max(min_value,result)

# print(result)

# 2 for loop
N,M=map(int,input().split())
print(M)
result=-1
cards=[]
for idx in range(N):
    cards=list(map(int,input().split()))
    min_value=1000
    for col in range(M):
        print(col)
        min_value=min(min_value,cards[col])
    result=max(min_value,result)

print(result)