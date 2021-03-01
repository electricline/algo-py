n, m = map(int, input().split())

num_list = [i + 1 for i in range(n)]
check_list = [False] * n

arr = []


def dfs(idx, depth):
    if depth == m:
        print(*arr)
        return

    for i in range(idx, n):
        if check_list[i]:
            continue

        check_list[i] = True
        arr.append(num_list[i])
        dfs(i, depth + 1)
        arr.pop()
        check_list[i] = False


dfs(0, 0)
