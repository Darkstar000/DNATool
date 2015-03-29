__author__ = 'Ruian'

if __name__ == "__main__":
    from dna_sort import DNASort

    c_1 = None
    c_2 = None
    c_4 = None
    is_running = True
    sort = DNASort()

    while is_running:
        print("Please chose what action to undertake")

        # Choose whether to replicate or translate
        while c_1 is None:
            c_1 = input("Choose an action: rep - Replicate DNA/RNA, "
                        "tlate - Translate DNA into proteins \n")
            if c_1 != "rep" and c_1 != "tlate":
                print("Please enter either rep or tlate")
                c_1 = None
        # Choice replication
        if c_1 == "rep":
            # Choice DNA/RNA
            while c_2 is None:
                c_2 = input("Choose whether to generate RNA or DNA \n")
                if c_2 == "RNA":
                    rna = sort.replicate(True)
                    print("The RNA strand is: " + sort.RNA_strand)
                    # Ask if user wishes to save
                    sort.fm.write(c_2, rna, sort.DNA_strand)
                elif c_2 == "DNA":
                    dna = sort.replicate(False)
                    print("The anti parallel strand is: " + sort.anti_strand)
                    # Ask if user wishes to save
                    sort.fm.write(c_2, dna, sort.DNA_strand)
                else:
                    print("Please enter either RNA or DNA")
                    c_2 = None
        # Choice translate
        elif c_1 == "tlate":
            prot = sort.translate()
            print("The associated protein is: " + sort.protein_sequence)
            sort.fm.write("prot", prot, sort.DNA_strand)

        # Ask user if they wish to do another action
        while c_4 is None:
            c_4 = input("Choose another action? (Y/N) \n")
            if c_4 == "Y":
                c_1 = None
                c_2 = None
            elif c_4 == "N":
                input("Press enter to exit. Thanks for using DNATool!")
                is_running = False
            else:
                print("Please enter Y or N")
                c_4 = None
        c_4 = None

