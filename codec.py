from sys import getsizeof


class CompressedGene:
    def __init__(self, gene):
        self._compress(gene)
    
    def _compress(self, gene):
        self.bit_string = 1
        for nucleotide  in gene.upper():
            self.bit_string <<= 2
            if nucleotide == "A":
                self.bit_string |= 0b00
            elif nucleotide == "C":
                self.bit_string |= 0b01
            elif nucleotide == "G":
                self.bit_string |= 0b10
            elif nucleotide == "T":
                self.bit_string |= 0b11
            else:
                raise ValueError("Invalid Nucleotide:{}".format(nucleotide))
    
    def decompress(self) -> str:
        gene = ""
        for i in range(0, self.bit_string.bit_length() - 1, 2):
            bits = self.bit_string >> i & 0b11 # get just 2 relevant bits
            if bits == 0b00: # A
                gene += "A"
            elif bits == 0b01: # C
                gene += "C"
            elif bits == 0b10: # G
                gene += "G"
            elif bits == 0b11: # T
                gene += "T"
            else:
                raise ValueError("Invalid bits:{}".format(bits))
        return gene[::-1] # [::-1] reverses string by slicing backward
    
    def __str__(self): # string representation for pretty printing
        return self.decompress()



