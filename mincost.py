import itertools
dist=[[0,10,15,20,],
      [5,0,9,10],
      [6,13,0,12],
      [8,8,9,0]]
lst=[0,1,2,3]
cost=99999999
per=set(itertools.permutations(lst))
for x in per:
    check=dist[x[0]][x[1]]+dist[x[1]][x[2]]+dist[x[2]][x[3]]+dist[x[3]][x[0]]
    cost=min(check,cost)
    print(x,x[0],cost)
