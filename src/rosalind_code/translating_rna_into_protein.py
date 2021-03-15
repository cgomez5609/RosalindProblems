from pathlib import Path

from pprint import PrettyPrinter

FILENAME = "rosalind_prot.txt"
TABLE_FILENAME = "rna_codon_table.txt"


def get_protein_string(rna_string: str, codon_table: dict) -> str:
    protein_string = ""
    for i in range(0, len(rna_string), 3):
        text_to_encode = rna_string[i] + rna_string[i + 1] + rna_string[i + 2]
        if codon_table[text_to_encode] == "Stop":
            break
        protein_string += codon_table[text_to_encode]

    return protein_string


def get_table(filename):
    table_path = Path().absolute().parent.parent / "tables"
    table = dict()
    full_table_path = table_path / filename
    with open(full_table_path, 'r') as f:
        data = f.read().split()
        for i in range(0, len(data), 2):
            table[data[i]] = data[i + 1]
        f.close()
    return table


def main(filename):
    pprint = PrettyPrinter()

    data_path = Path().absolute().parent.parent / "data"
    full_path = data_path / filename
    table = get_table(TABLE_FILENAME)
    print(pprint.pprint(table))

    with open(full_path, 'r') as f:
        data = f.read().rstrip()
        ans = get_protein_string(rna_string=data, codon_table=table)
        print(ans)
        f.close()


if __name__ == '__main__':
    main(filename=FILENAME)
