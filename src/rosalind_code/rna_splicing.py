from pathlib import Path
from pprint import PrettyPrinter

from codon_table import get_codon_table
from transcribing_dna_into_rna import dna_into_rna
from translating_rna_into_protein import get_protein_string

FILENAME = "rosalind_splc.txt"

pp = PrettyPrinter()


def format_data(data):
    f_data = dict()
    f_data["dna"] = "".join(data[1].split("\n")[1::])
    f_data["introns"] = list()
    for i in range(2, len(data)):
        temp = data[i].split("\n")
        f_data["introns"].append(temp[1])
    return f_data


def rna_to_protein(data, table):
    s = data["dna"]
    s1 = data["introns"][0]

    for sub_s in data["introns"]:
        index = s.index(sub_s)
        new_s = s[0:index] + s[index+len(sub_s)::]
        s = new_s

    rna_string = dna_into_rna(s)
    protein_string = get_protein_string(rna_string=rna_string, codon_table=table)

    return protein_string


def main(filename=FILENAME):
    pp = PrettyPrinter()

    data_path = Path().absolute().parent.parent / "data"
    full_path = data_path / filename
    
    codon_table = get_codon_table()

    with open(full_path) as f:
        data = f.read().split(">")
        data = format_data(data=data)
        pp.pprint(data)
        protein_string = rna_to_protein(data=data, table=codon_table)
        print(protein_string)
        f.close()


if __name__ == '__main__':
    main()