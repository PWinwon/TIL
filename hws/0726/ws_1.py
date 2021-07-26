def get_dict_avg(scores):
    total = 0
    for score in scores.values():
        total += score
    return total/len(scores)

    

a = get_dict_avg({
    'python' : 80,
    'algorithm' : 90,
    'django' : 89,
    'web' : 83,
})
print(a)