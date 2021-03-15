from pathlib import Path

FILENAME = "rosalind_fibd.txt"

def fib(n, m):
    table = [0] * (n+1)
    table[0] = 1
    table[1] = 1
    table[2] = 1

    for i in range(3, n+1):
        if (i - m) < 0:
            start = 0
        else:
            start = (i - m)
        end = (i - 1)
        table[i] = sum(table[start:end])

    return table[n]


def wabbit_season(n, m):
    result = fib(n=n, m=m)
    return result


def main(filename):
    data_path = Path().absolute().parent.parent / "data"
    full_path = data_path / filename

    matrix = list()
    with open(full_path, 'r') as f:
        data = f.read().rstrip()
        data = data.split()
        print(data[0], data[1])
        n = int(data[0])
        m = int(data[1])
        ans = wabbit_season(n=n, m=m)
        print(ans)
        f.close()


if __name__ == '__main__':
    main(filename=FILENAME)
