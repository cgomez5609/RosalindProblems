from pathlib import Path

filename = ""

def get_dna_nucleotide_count(string):
    dna_count = dict()
    dna_count["A"] = 0
    dna_count["C"] = 0
    dna_count["G"] = 0
    dna_count["T"] = 0
    for letter in string:
        dna_count[letter.upper()] += 1
    return dna_count["A"], dna_count["C"], dna_count["G"], dna_count["T"]

def main(filename):
    data_path = Path().absolute().parent.parent / "data"
    full_path = data_path / filename


    values = None
    with open(full_path, 'r') as f:
        data = f.read().rstrip()
        data = data.split(">")
        f.close()
