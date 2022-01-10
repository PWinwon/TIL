def merge_sort(n, arr):

    def my_sort(start, end):
        if end - start < 2:
            return
        mid = (start + end) // 2

        my_sort(start, mid)
        my_sort(mid, end)

        merge(start, mid, end)

    def merge(start, mid, end):
        temp = []

        s, e = start, mid

        while s < mid and e < end:
            if arr[s] < arr[e]:
                temp.append(arr[s])
                s += 1
            else:
                temp.append(arr[e])
                e += 1

        while s < mid:
            temp.append(arr[s])
            s += 1

        while e < end:
            temp.append(arr[e])
            e += 1


        for i in range(start, end):
            arr[i] = temp[i-start]

    return my_sort(0, len(arr))


N = int(input())

lst = []

for n in range(N):
    lst.append(int(input()))

merge_sort(N, lst)

for n in range(N):
    print(lst[n])