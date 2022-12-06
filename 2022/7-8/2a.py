roads = [list(map(int, input().split())) for _ in range(int(input()))]
print(sum(sum(roads[i][i:]) for i in range(len(roads))))
