from pathlib import Path

FILENAME = "rosalind_revc.txt"


def reverse_complement(sequence):
    sequence = sequence[::-1]
    complement = ""
    for letter in sequence:
        if letter.upper() == "A":
            complement += "T"
        elif letter.upper() == "T":
            complement += "A"
        elif letter.upper() == "G":
            complement += "C"
        elif letter.upper() == "C":
            complement += "G"
    return complement


def main(filename):
    data_path = Path().absolute().parent.parent / "data"
    full_path = data_path / filename

    with open(full_path, 'r') as f:
        data = f.read().rstrip()
        ans = reverse_complement(sequence=data)
        print(ans)
        f.close()


if __name__ == '__main__':
    main(filename=FILENAME)