# # My Answer
# n=int(input()) # price

# a=[500,100,50,10,5,1]
# change=1000-n
# count=[0,0,0,0,0,0]
# index=0
# sum=0
# for i in a:
#     temp=change//i
#     change=change-i*temp
#     count[index]=temp
#     index=index+1

# for idx in range(len(count)):
#     sum=sum+count[idx]

# print(sum)

# Solution
n=int(input())
a=[500,100,50,10,5,1]
change=1000-n
count=0
for coin in a:
    count+=change//coin
    change%=coin

print(count)