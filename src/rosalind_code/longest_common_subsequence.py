def Longest_common_subsequence(a, b, table):
    for row in range(1, len(table)):
        for col in range(1, len(table[row])):
            if b[row-1] == a[col-1]:
                table[row][col] = table[row-1][col-1] + 1
            else:
                table[row][col] = max(table[row][col-1], table[row-1][col])