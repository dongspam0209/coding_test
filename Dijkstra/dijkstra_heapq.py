import heapq
INF=1000000
n,m=map(int,input().split())
start=int(input()) #시작 노드
graph=[[]for i in range(n+1)]
visited=[False]*(n+1) #해당 노드 방문여부
distance=[INF]*(n+1) #현재노드에서 해당노드까지의 거리

for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))
 

def dijkstra(start):
    priority_queue=[]
    heapq.heappush(priority_queue,(0,start))
    distance[start]=0
    while priority_queue:
        dist,next_node=heapq.heappop(priority_queue)
        if distance[next_node]<dist:
            continue
        for i in graph[next_node]:
            cost=dist+i[1]
            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(priority_queue,(cost,i[0]))
                
dijkstra(start)

for i in range(1,n+1):
    if distance[i]==INF:
        print("infinite")
    else:
        print(distance[i])