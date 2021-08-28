def my_func(level, total, l, tar, nums, ans):
    if level == l and total == tar:
        ans.append(1)
        return
    elif level == l:
        return
    my_func(level + 1, total + nums[level], l, tar, nums, ans)
    my_func(level + 1, total - nums[level], l, tar, nums, ans)
    return
        

def solution(numbers, target):
    answer = 0
    result = []
    my_func(0, 0, len(numbers), target, numbers, result)
    answer = len(result)
    return answer