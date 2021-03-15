from pathlib import Path
from pprint import PrettyPrinter

FILENAME = "rosalind_cons.txt"


def get_dna_base_profile(matrix):
    consensus_string = ""
    dna_base_profile = dict()
    dna_base_profile["A"] = [0] * len(matrix[0])
    dna_base_profile["C"] = [0] * len(matrix[0])
    dna_base_profile["G"] = [0] * len(matrix[0])
    dna_base_profile["T"] = [0] * len(matrix[0])
    for col in range(len(matrix[0])):
        for row in range(len(matrix)):
            base = matrix[row][col]
            dna_base_profile[base][col] += 1
        consensus_string += get_consensus_base(dna_base_profile=dna_base_profile, index=col)
    return dna_base_profile, consensus_string


def get_consensus_base(dna_base_profile, index) -> str:
    highest_value = -1
    base = None
    for key, value in dna_base_profile.items():
        if value[index] > highest_value:
            highest_value = value[index]
            base = key
    return base


def print_dna_profile(dna_profile: dict):
    dna_profile["A"] = [str(l) for l in dna_profile["A"]]
    print("A:", " ".join(dna_profile["A"]))
    dna_profile["C"] = [str(l) for l in dna_profile["C"]]
    print("C:", " ".join(dna_profile["C"]))
    dna_profile["G"] = [str(l) for l in dna_profile["G"]]
    print("G:", " ".join(dna_profile["G"]))
    dna_profile["T"] = [str(l) for l in dna_profile["T"]]
    print("T:", " ".join(dna_profile["T"]))


def main(filename):
    data_path = Path().absolute().parent.parent / "data"
    full_path = data_path / filename

    # to print the matrix and dna profile in a readable manner
    # pp = PrettyPrinter()

    matrix = list()
    with open(full_path, 'r') as f:
        data = f.read().rstrip()
        data = data.split(">")
        for i in range(1, len(data)):
            line = data[i].split()
            entry = "".join(line[1::])
            matrix.append(list(entry))
        f.close()

    dna_profile, consensus_string = get_dna_base_profile(matrix)
    print(consensus_string)
    print_dna_profile(dna_profile=dna_profile)


if __name__ == '__main__':
    main(filename=FILENAME)
