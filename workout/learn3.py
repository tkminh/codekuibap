list_to_sort = [27, 0, 71, 15, 22, 70, 27, 63, 90, 50, 60 , 70, 89, 25, 34, 34, 76, 32, 23, 1, 7, 9, 50 , 100, 21, 51, 43, 67, 41]
list_to_sort2 = list_to_sort.copy()


def bubble_sort(lst):
    step = 0
    for border in range(len(lst) - 1, 0, -1):
        for i in range(border):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
                step = step + 1
    print("Steps BB sort: " + str(step))
    return lst

def my_sort(lst):
    step = 0
    for i in range(len(lst)-1):
        for j in range(i, len(lst)):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
                step = step + 1
    print("Steps my sort: " + str(step))
    return lst

print(bubble_sort(list_to_sort))

print(my_sort(list_to_sort2))