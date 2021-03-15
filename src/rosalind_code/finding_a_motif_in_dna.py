from pathlib import Path

FILENAME = "rosalind_subs.txt"


def combing_through_the_haystack(s: str, t: str) -> str:
    indices = list()
    t_length = len(t)
    for i in range(len(s)):
        if s[i] == t[0]:
            if s[i:i+t_length] == t:
                indices.append(str(i+1))
    print(" ".join(indices))
            

def main(filename):

    data_path = Path().absolute().parent.parent / "data"
    full_path = data_path / filename

    with open(full_path, 'r') as f:
        data = f.read().split("\n")
        combing_through_the_haystack(s=data[0], t=data[1])
        f.close()


if __name__ == '__main__':
    main(filename=FILENAME)
