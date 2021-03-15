from codon_table import get_reverse_codon_table

from pathlib import Path
from pprint import PrettyPrinter

FILENAME = "rosalind_mrna.txt"

def get_total_different_rna_strings_count(data, table):
    data_list = list(data)
    count = 1
    
    for letter in data_list:
        length = len(table[letter])
        count *= length
    
    count *= len(table["Stop"])
    return count % 1000000
    

def main(filename=FILENAME):
    pp = PrettyPrinter()

    data_path = Path().absolute().parent.parent / "data"
    full_path = data_path / filename

    r_codon_table = get_reverse_codon_table()
    pp.pprint(r_codon_table)

    with open(full_path) as f:
        data = f.read().rstrip()
        ans = get_total_different_rna_strings_count(data=data, table=r_codon_table)
        print(ans)
        f.close()


if __name__ == '__main__':
    main()