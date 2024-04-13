INF=1000000
n,m=map(int,input().split())
start=int(input()) #시작 노드
graph=[[]for i in range(n+1)]
visited=[False]*(n+1) #해당 노드 방문여부
distance=[INF]*(n+1) #현재노드에서 해당노드까지의 거리

for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))

def get_smallest_node():
    min_value=INF
    index=0
    for i in range(1,n+1):
        if distance[i]<min_value and not visited[i]:
            min_value=distance[i]
            index=i
            
    return index
def dijsktra(start):
    distance[start]=0
    visited[start]=True
    for j in graph[start]:
        distance[j[0]]=j[1]  
        #j=(2,2) (3,5) (4,1) j[0]=2,3,4 다음으로 갈 수 있는 노드 j[1]=2,5,1 갈 수 있는 노드에 대한 거리
    for i in range(n-1): # 시작노드를 제외한 나머지 노드 다 방문할 횟수만큼만 실행하면 되서 사실 i는 사용하지않음
        now=get_smallest_node()
        visited[now]=True
        for j in graph[now]:
            cost=distance[now]+j[1]
            if cost<distance[j[0]]:
                distance[j[0]]=cost

dijsktra(start)

for i in range(1,n+1):
    if distance[i]==INF:
        print("infinite")
    else:
        print(distance[i])
        
