from utils import measure_sorting_time

@measure_sorting_time
def bubble_sort(_list):
    for i in range(len(_list) - 1):
        for j in range(len(_list)-1-i):
            if _list[j] > _list[j+1]:
                _list[j], _list[j+1] = _list[j+1], _list[j]
    return _list


@measure_sorting_time
def selection_sort(_list):
    for i in range(len(_list)-1):
        curr_min_idx = i
        for j in range(i+1, len(_list)):
            if _list[j] < _list[curr_min_idx]:
                curr_min_idx = j
        _list[i], _list[curr_min_idx] = _list[curr_min_idx], _list[i]
    return _list


@measure_sorting_time
def quick_sort(_list):
    def order_sublist(_list, first_idx, last_idx):
        if first_idx == last_idx:
            return
        base_idx = first_idx-1
        swap_idx = first_idx-1
        pivot = _list[last_idx]
        for _ in range(first_idx, last_idx+1, 1):
            base_idx += 1
            if _list[base_idx] > pivot:
                continue
            swap_idx += 1
            _list[base_idx], _list[swap_idx] = _list[swap_idx], _list[base_idx]
        order_sublist(_list, first_idx, max(swap_idx-1, first_idx))
        order_sublist(_list, min(swap_idx+1, last_idx), last_idx)
    order_sublist(_list, 0, max(len(_list)-1, 0))
    return _list


@measure_sorting_time
def merge_sort(_list):
    def merge(arr, l, m, r):
        n1 = m - l + 1
        n2 = r - m

        L = [0] * (n1)
        R = [0] * (n2)

        for i in range(0, n1):
            L[i] = arr[l + i]

        for j in range(0, n2):
            R[j] = arr[m + 1 + j]

        i = 0
        j = 0
        k = l

        while i < n1 and j < n2:
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < n1:
            arr[k] = L[i]
            i += 1
            k += 1

        while j < n2:
            arr[k] = R[j]
            j += 1
            k += 1

    def mergeSort(arr, l, r):
        if l < r:

            m = l+(r-l)//2
            mergeSort(arr, l, m)
            mergeSort(arr, m+1, r)
            merge(arr, l, m, r)
    mergeSort(_list, 0, len(_list)-1)
    return _list


@measure_sorting_time
def insertion_sort(arr):
    n = len(arr)

    if n <= 1:
        return

    for i in range(1, n):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
