N, K = map(int, input().split())

bag = [0] * (K+1)

for n in range(N):
    w, v = map(int, input().split())
    
    if w > K:
        continue

    for idx in range(K, -1, -1):
        if bag[idx] != 0 and idx+w <= K:
            bag[idx+w] = max(bag[idx+w], bag[idx] + v)

    bag[w] = max(v, bag[w])

print(max(bag))