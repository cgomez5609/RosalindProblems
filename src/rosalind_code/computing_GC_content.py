from pathlib import Path

FILENAME = "rosalind_gc.txt"


def gc_content(sequence: str):
    g_count = sequence.count("G")
    c_count = sequence.count("C")

    result = ((g_count + c_count) / len(sequence)) * 100
    
    return round(result, 6)


def main(filename):
    data_path = Path().absolute().parent.parent / "data"
    full_path = data_path / filename

    best_value = 0.0
    roslaind_id = None
    with open(full_path, 'r') as f:
        data = f.read().rstrip()
        data = data.split(">")
        for i in range(1, len(data)):
            lines = data[i].split("\n")
            title = lines[0]
            sequence = "".join(lines[1::])
            ans = gc_content(sequence=sequence)
            if ans > best_value:
                best_value = ans
                roslaind_id = title
        print(roslaind_id)
        print(best_value)
        f.close()


if __name__ == '__main__':
    main(filename=FILENAME)