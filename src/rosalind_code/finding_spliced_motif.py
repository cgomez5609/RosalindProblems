from pathlib import Path
from pprint import PrettyPrinter

import numpy as np

FILENAME = "rosalind_sseq.txt"

pp = PrettyPrinter()


def get_values(data):
    values = dict()
    values["dna_string"] = "".join(data[1].split("\n")[1::])
    values["t"] = "".join(data[2].split("\n")[1::])
    return values


def longest_common_subsequence(a, b, table):
    for row in range(1, len(table)):
        for col in range(1, len(table[row])):
            if b[row - 1] == a[col - 1]:
                table[row][col] = table[row - 1][col - 1] + 1
            else:
                table[row][col] = max(table[row-1][col], table[row][col-1])

    row = len(table) - 1
    col = len(table[0]) - 1
    end = table[row][col]
    indices = list()
    while end != 1 and row > 0 and col > 0:
        left = table[row][col - 1]
        up = table[row - 1][col]
        diag = table[row - 1][col - 1]
        index = np.argmax([left, up, diag])
        if left == diag and diag == up:
            indices.append(col)
            row = row - 1
            col = col - 1
            end = table[row][col]
        else:
            col = col - 1
    indices.append(col)
    indices = indices[::-1]

    result = [str(i) for i in indices]

    return " ".join(result)


def main(filename):
    data_path = Path().absolute().parent.parent / "data"
    full_path = data_path / filename

    values = None
    with open(full_path, 'r') as f:
        data = f.read().rstrip()
        data = data.split(">")
        values = get_values(data)
        f.close()
    # pp.pprint(values)
    a = values["dna_string"]
    b = values["t"]
    table = np.zeros((len(b) + 1, len(a) + 1), dtype=int)
    ans = longest_common_subsequence(a, b, table)
    print(ans)


if __name__ == '__main__':
    main(filename=FILENAME)