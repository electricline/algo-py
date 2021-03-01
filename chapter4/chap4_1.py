n = int(input())
r, c = 1, 1
direction = input().split()

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]
move = ['L', 'R', 'U', 'D']

for dirc in direction:
    for i in range(len(move)):
        if dirc == move[i]:
            nr = r + dr[i]
            nc = c + dc[i]
    if nr < 1 or nc < 1 or nr > n or nc > n:
        continue
    r, c = nr, nc

print(r, c)
