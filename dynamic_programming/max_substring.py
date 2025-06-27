def get_valid_value(matrix, i, j):
    if i < 0 or j < 0:
        return 0
    return matrix[i][j]

def max_substring(word1, word2):
    n = len(word1)
    m = len(word2)
    matrix = [[0 for _ in range(n)] for _ in range(m)]
    max_len = 0

    for i in range(n):
        for j in range(m):
            if word1[i] == word2[j]:
                matrix[i][j] += 1
                if i > 0 and j > 0:
                    matrix[i][j] += matrix[i - 1][j - 1]
                if matrix[i][j] > max_len:
                    max_len = matrix[i][j]
    print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in matrix]))
    print(max_len)

def max_common_subsequence(word1, word2):
    n = len(word1)
    m = len(word2)
    matrix = [[0 for _ in range(n)] for _ in range(m)]

    for i in range(n):
        for j in range(m):
            if word1[i] == word2[j]:
                matrix[i][j] += 1
                if i > 0 and j > 0:
                    matrix[i][j] += matrix[i - 1][j - 1]
            else:
                matrix[i][j] = max(
                    get_valid_value(matrix, i - 1, j),
                    get_valid_value(matrix, i, j - 1)
                )

    print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in matrix]))
    print(matrix[-1][-1])

word1 = 'fish'
word2 = 'fosh'
max_substring(word1, word2)
max_common_subsequence(word1, word2)
