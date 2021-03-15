from pathlib import Path
from pprint import PrettyPrinter

import numpy as np

FILENAME = "rosalind_lcsm.txt"

def get_values(data):
    values = dict()
    for i in range(1, len(data)):
        value = data[i].split("\n")
        values[value[0]] = "".join(value[1::])
    return values


def get_shortest_string(values):
    a = None
    length = 2000
    for key, value in values.items():
        if len(value) < length:
            length = len(value)
            a = key

    b = None
    length = 2000
    for key, value in values.items():
        if key != a:
            if len(value) < length:
                length = len(value)
                b = key
    return a, b


def main(filename):
    data_path = Path().absolute().parent.parent / "data"
    full_path = data_path / filename
    
    pp = PrettyPrinter()
    values = None
    with open(full_path, 'r') as f:
        data = f.read().rstrip()
        data = data.split(">")
        values = get_values(data)
        f.close()
    #pp.pprint(values)
    choice_a, choice_b = get_shortest_string(values)
    a = values[choice_a]
    b = values[choice_b]
    table = np.zeros((len(b)+1, len(a)+1), dtype=int)
    lcs_list = longest_common_substring(a, b, table)
    values.pop(choice_a, None)
    values.pop(choice_b, None)
    lcs = check_other_strings(lcs_list, values)
    print("The longest common substring is:", lcs)


def longest_common_substring(a, b, table):
    lcs_list = list()
    for row in range(1, len(table)):
        for col in range(1, len(table[row])):
            if b[row-1] == a[col-1]:
                table[row][col] = table[row-1][col-1] + 1
            else:
                table[row][col] = 0

    max_value = np.amax(table) # get largest value
    row, col = np.where(table == max_value) # get indices of the largest value
    row = row[0]
    col = col[0]
    end = table[row][col]
    longest_substring = b[row-1]
    while end != 1 and row > 0 and col > 0:
        left = table[row][col-1]
        up = table[row-1][col]
        diag = table[row-1][col-1]
        index = np.argmax([left, up, diag])
        if index == 2:  # diag
            end = end - 1
            row = row - 1
            col = col - 1
            longest_substring += b[row-1]
            if end == 1:
                lcs_list.append(longest_substring[::-1])
                if row > 0  and col > 0:
                    slice = table[0:row+1, 0:col+1]
                    max_value = np.amax(slice)
                    row, col = np.where(slice == max_value)
                    row = row[0]
                    col = col[0]
                    end = table[row][col]
                    longest_substring = b[row-1]
        elif index == 1:  # up
            row = row - 1
        else:  # left
            col = col - 1

    return lcs_list

def check_other_strings(lcs_list, values):
    common = None
    for lcs in lcs_list:
        temp_lcs = lcs
        while len(temp_lcs) > 1:
            in_all = True
            for key, value in values.items():
                if temp_lcs not in value:
                    in_all = False
                    break
            if in_all:
                if common is None:
                    common = temp_lcs
                elif len(temp_lcs) > len(common):
                    common = temp_lcs
            temp_lcs = temp_lcs[0:-1]
    return common

if __name__ == '__main__':
    main(filename=FILENAME)
