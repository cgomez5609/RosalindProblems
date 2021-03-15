from pathlib import Path

FILENAME = "rosalind_hamm.txt"


def hamming_distance(sequence_a: str, sequence_b: str):
    count = 0
    assert(len(sequence_a) == len(sequence_b))

    for i in range(len(sequence_a)):
        if sequence_a[i] != sequence_b[i]:
            count += 1
    return count


def main(filename):
    data_path = Path().absolute().parent.parent / "data"
    full_path = data_path / filename

    best_value = 0.0
    roslaind_id = None
    with open(full_path, 'r') as f:
        data = f.read().split("\n")
        seq_a = data[0]
        seq_b = data[1]
        ans = hamming_distance(sequence_a=seq_a, sequence_b=seq_b)
        print(ans)
        f.close()


if __name__ == '__main__':
    main(filename=FILENAME)

