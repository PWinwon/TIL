def solution(genres, plays):
    answer = []
    hash_cnt = {}
    hash_val = {}
    hash_idx = {}
    for idx in range(len(genres)):
        if genres[idx] in hash_cnt:
            hash_cnt[genres[idx]] += plays[idx]
            hash_val[genres[idx]].append(plays[idx])
            hash_idx[genres[idx]].append(idx)
        else:
            hash_cnt[genres[idx]] = plays[idx]
            hash_val[genres[idx]] = [plays[idx]]
            hash_idx[genres[idx]] = [idx]
    hash_cnt = sorted(hash_cnt.items(), key=lambda x: x[1], reverse=True)
    temp = []
    for i in hash_cnt:
        temp.append(i[0])
    for t in temp:
        for i in range(2):
            max_val = max(hash_val[t])
            if i == 1 and len(hash_val[t]) == 1:
                break
            for j in range(len(hash_val[t])):
                if hash_val[t][j] == max_val:
                    answer.append(hash_idx[t][j])
                    hash_val[t][j] = 0
                    break
    return answer