import csv

PATH_TO_FILE = "input_files/ex2-2/genetic_code.csv"

# global sets of special codons, they will be filled while reading the file
START_CODONS = set()
STOP_CODONS = set()

def read_genetic_code(file_name):

    code = {}

    try:
        with open(file_name, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            for items in reader:
                aminoacid = items[0].strip()
                codons = items[1].strip().split(',')  # the second field contained a comma-delimited list
                codons = [codon.strip() for codon in codons]  # remove spaces inside each codon

                # for aminoacid, populate the dict:
                if aminoacid != 'start' and aminoacid != 'stop':
                    for codon in codons:
                        code[codon] = aminoacid
                elif aminoacid == 'start':
                    for codon in codons:
                        START_CODONS.add(codon)
                elif aminoacid == 'stop':
                    for codon in codons:
                        STOP_CODONS.add(codon)
        return code
    except OSError as ex:
        exit(f"Error openning file {ex}")


def decode(code, dna):
    start = 0

    protein = ''

    # search for START codon
    while start < len(dna) - 2 and dna[start:start + 3] not in START_CODONS:
        start = start + 1

    if start == len(dna) - 2:
        print("START codon not found")
        return

    while start < len(dna) - 2 and dna[start:start + 3] not in STOP_CODONS:
        aminoacid = code[dna[start:start + 3]]
        protein = protein + aminoacid
        start = start + 3

    if dna[start:start + 3] not in STOP_CODONS:
        print("STOP codon not found")
        return

    print(protein)


def main():
    genetic_code = read_genetic_code(PATH_TO_FILE)

    dna = input("Insert a DNA fragment: ").upper()

    decode(genetic_code, dna)


if __name__ == "__main__":

    main()
