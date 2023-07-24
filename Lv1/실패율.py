def solution(N, stages):
    p = []
    cnt = [stages.count(i) for i in range(1, N + 1)]
    for i, n in enumerate(range(1, N + 1)):
        if cnt[i] == 0:
            p.append((i + 1, 0))
            continue
        p.append((i + 1, cnt[i] / len(list(filter(lambda x: x >= n, stages)))))
    p.sort(reverse=True, key=lambda x: x[1])
    return [e[0] for e in p]


assert solution(5, [2, 1, 2, 6, 2, 4, 3, 3]) == [3, 4, 2, 1, 5]
assert solution(4, [4, 4, 4, 4, 4]) == [4, 1, 2, 3]

# N = total # of stages, stages contain current users' stage that they have to clear.
# If the current stage == N + 1, it means that the user passed the entire stage.
# Return the stages based on the failure rate following the descending order.
