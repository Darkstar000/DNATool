__author__ = 'Ruian'

class FileManager:
    """
    Represents a file managing system

    current_file - str: The file currently being parsed
    write_file - str: The file currently being written
    """

    def __init__(self):
        """(FileManager, DNASort) -> NoneType

        Initialize file management program
        """

        self.current_file = None

    def import_file(self):
        """(FileManager) -> NoneType

        Import a file for parsing
        """

        while self.current_file is None:
            try:
                file = input("Please enter the name of the file: \n")
                self.current_file = open(file, 'r')
            except IOError:
                print("Invalid file")

    def reopen(self, wipe, strand):
        """(FileManager, boolean, list) -> NoneType

        Re-import a file for parsing. Wipe DNA sequence if wipe is True
        """

        self.current_file.close()
        self.current_file = None
        if wipe:
            strand = []
        self.import_file()

    def write(self, strand_type, strand_data, original_strand=None):
        """(FileManager, str, str, str) -> NoneType

        Write the results of a replication or translation into a file. Name
        file RNA_strand if strand is RNA, or Anti_strand if strand is DNA,
        unless user specifies file name.
        """

        c_3 = None
        c_4 = None
        # Default name
        if strand_type == "RNA":
            name = "RNA_strand.txt"
        elif strand_type == "DNA":
            name = "Anti_strand.txt"
        else:
            name = "Protein.txt"
        # Ask user if they wish to save
        while c_3 is None:
            c_3 = input("Do you wish to save this result? (Y/N) \n")
            if c_3 == "Y":
                # Ask user if they want to choose file name
                while c_4 is None:
                    c_4 = input("Do you wish to choose the file name? (Y/N) "
                                "\n")
                    if c_4 == "Y":
                        name = input("Enter file name (exclude .txt) \n") + \
                            ".txt"
                        self.write_file = open(name, "a")
                    elif c_4 == "N":
                        self.write_file = open(name, "a")
                    else:
                        print("Please enter either Y or N")
                        c_4 = None
                # Determine print based on strand type
                if strand_type == "RNA":
                    print(original_strand, file=self.write_file)
                    print(strand_data, file=self.write_file)
                elif strand_type == "DNA":
                    print(original_strand, file=self.write_file)
                    print(strand_data, file=self.write_file)
                else:
                    print(original_strand, file=self.write_file)
                    print(strand_data, file=self.write_file)
                self.write_file.close()
            elif c_3 != "N":
                print("Please enter Y or N")
                c_3 = None
