from pathlib import Path
from pprint import PrettyPrinter

FILENAME = "rosalind_grph.txt"

def make_values(data):
    values = dict()

    for i in range(1, len(data)):
        lines = data[i].split("\n")
        if lines[0] not in values:
            values[lines[0]] = lines[1] + lines[2]
    return values

def make_graph(values, k=3):
    graph = dict()
    
    for key, value in values.items():
        suffix = value[len(value)-k::]
        for o_key, o_value in values.items():
            if key != o_key:
                prefix = o_value[0:k]
                if suffix == prefix:
                    print(key, o_key)

def main(filename):
    data_path = Path().absolute().parent.parent / "data"
    full_path = data_path / filename

    pp = PrettyPrinter()
    values = None
    with open(full_path, 'r') as f:
        data = f.read().rstrip()
        data = data.split(">")
        values = make_values(data)
        f.close()
    pp.pprint(values)
    make_graph(values)

if __name__ == '__main__':
    main(filename=FILENAME)
