TABLE = dict()
TABLE[0] = 0
TABLE[1] = 1

def fib(n, k, table):
    if n in table:
        return table[n]

    table[n] = fib(n-1, k, table) + fib(n-2, k, table) * k
    return (table[n-1] + (table[n-2] * 3))


def wascally_rabbits(n, k):
    result = fib(n=n, k=k, table=TABLE)
    return result
