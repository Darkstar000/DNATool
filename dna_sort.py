__author__ = 'Ruian'
from file_manager import FileManager

class DNASort:
    """
    Represents a DNA sorter

    DNA_strand - list/str: The DNA strand being analyzed
    anti_strand - str: The anti-parallel DNA strand
    RNA_strand - str: The RNA strand complimentary to the DNA strand
    protein_sequence -str: The protein sequence associated with the DNA strand
    """

    def __init__(self):
        """(DNASort) -> NoneType

        Initialize DNA sorting object
        """
        self.AA_dictionary = {'TTT':'PHE', 'TTC':'PHE', 'TTA':'LEU','TTG':'LEU','CTT':'LEU','CTC':'LEU',
         'CTA':'LEU','CTG':'LEU','ATT':'LLE','ATC':'LLE','ATA':'LLE','ATG':'MET',
         'GTT':'VAL','GTC':'VAL','GTA':'VAL','GTG':'VAL','TCT':'SER','TCC':'SER',
         'TCA':'SER','TCG':'SER','CCT':'PRO','CCC':'PRO','CCA':'PRO','CCG':'PRO',
         'ACT':'THR','ACC':'THR','ACA':'THR','ACG':'THR','GCT':'ALA','GCC':'ALA',
         'GCA':'ALA','GCG':'ALA','TAT':'TYR','TAC':'TYR','TAA':'STOP','TAG':'STOP',
         'CAT':'HIS','CAC':'HIS','CAA':'GLN','CAG':'GLN','AAT':'ASN','AAC':'ASN',
         'AAA':'LYS','AAG':'LYS','GAT':'ASP','GAC':'ASP','GAA':'GLU','GAG':'GLU',
         'TGT':'CYS','TGC':'CYS','TGA':'STOP','TGG':'TRP','CGT':'ARG','CGC':'ARG',
         'CGA':'ARG','CGG':'ARG','AGT':'SER','AGC':'SER','AGA':'ARG','AGG':'ARG',
         'GGT':'GLY','GGC':'GLY','GGA':'GLY','GGG':'GLY'}
        self.fm = FileManager()
        self.DNA_strand = []
        self.fm.import_file()
        self.import_sequence()

    def import_sequence(self):
        """(DNASort) -> NoneType

        Import the DNA sequence from the current file, and add it to
        DNA sequence. If DNA sequence is correctly formatted, convert to string

        Precondition: Each nucleotide must be a G,T,C, or A, and no spaces are
        permitted.
        """

        self.DNA_strand = self.fm.current_file.readlines()
        # Ensure DNA made of correct nucleotides
        dna = ""
        for sequence in self.DNA_strand:
            for char in sequence:
                char = char.upper()
                if char not in "GTCA" and char != "\n":
                    print("Error, please enter valid nucleotides")
                    self.fm.reopen(True, self.DNA_strand)
                else:
                    if char != "\n":
                        dna += char
        self.DNA_strand = dna.upper()
        print("The DNA template strand is :" + self.DNA_strand)

    def replicate(self, RNA):
        """(DNASort, boolean) -> str

        Generate anti-parallel DNA strand based on a single strand. Generate
        RNA strand if RNA parameter is True.
        """
        if RNA:
            self.RNA_strand = ""
        else:
            self.anti_strand = ""

        for char in self.DNA_strand:
            if RNA:
                self.RNA_strand += self.generate_base_pair(char, RNA)
            else:
                self.anti_strand += self.generate_base_pair(char, RNA)

        return self.RNA_strand if RNA else self.anti_strand

    def generate_base_pair(self, base_pair, RNA):
        """(DNASort, str, boolean) -> str

        Return the complimentary base pair of the base_pair. RNA determines
        whether A returns U (For RNA) or T (For DNA).
        """

        if base_pair == "A":
            if RNA:
                return "U"
            else:
                return "T"
        elif base_pair == "G":
            return "C"
        elif base_pair == "T":
            return "A"
        elif base_pair == "C":
            return "G"

    def translate(self):
        """(DNASort) -> str

        Return the amino acid sequence associated with the DNA sequence
        based on the AA_dictionary.
        """

        self.protein_sequence = ""

        codon = ""
        is_started = False
        for char in self.DNA_strand:
            # Looks for start codon
            if not is_started:
                codon += char
                if "ATG" in codon:
                    is_started = True
                    self.protein_sequence += "MET "
                    codon = ""
            else:
                codon += char
                if len(codon) == 3:
                    self.protein_sequence += (self.AA_dictionary[codon] + " ")
                    codon = ""

        return self.protein_sequence