from pathlib import Path

TABLE_FILENAME = "rna_codon_table.txt"

def get_codon_table():
    table_path = Path().absolute().parent.parent / "tables"
    table = dict()
    full_table_path = table_path / TABLE_FILENAME
    if full_table_path.exists():
        with open(full_table_path, 'r') as f:
            data = f.read().split()
            for i in range(0, len(data), 2):
                table[data[i]] = data[i + 1]
            f.close()
        return table
    else:
        print("File not found at:", full_table_path)
        return None


def get_reverse_codon_table():
    codon_table = get_codon_table()
    reverse_codon_table = dict()
    for w in sorted(codon_table, key=codon_table.get):
        value = codon_table[w]
        if value not in reverse_codon_table:
            reverse_codon_table[value] = list()
            reverse_codon_table[value].append(w)
        else:
            reverse_codon_table[value].append(w)
    return reverse_codon_table