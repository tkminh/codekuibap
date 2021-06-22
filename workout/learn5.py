# selection sort
# https://www.educative.io/blog/python-algorithms-coding-interview

lst = [3, 2, 1, 5, 4, 6, 1, 2]

# find the min index and swap
def selection_sort(lst):
    for i in range(len(lst)):
        min_index = i
        for j in range(i+1, len(lst)):
            # check the item of min_index to get the min value
            if lst[min_index] > lst[j]: 
                min_index = j
        lst[i], lst[min_index] = lst[min_index], lst[i]
        
    print("Final" + str(lst))

selection_sort(lst)