matrix = [
    [3,4,4,6],
    [6,8,11,12],
    [6,8,11,15],
    [9,11,12,17]
]
def find_matrix(matrix, value):
    j = len(matrix) - 1
    for row in matrix:
        print(row)
        while row[j] > value:
            j -= 1
            if j < 0:
                return False
        if row[j] == value:
            return True
    return False
print(find_matrix(matrix,11))