# Made By Mohammed Hijazi
from typing import Dict, List
import sys 

OPTAB: Dict[str,str] = {}
SYMTAB: Dict[str,str] = {}
DIREC = ["RSUB","WORD","BYTE","RESW","RESB"]
PRGNAME = ""
CODE = []

def read_OPTAB() : 
    appendix = open("Appendix.txt","r")
    for line in appendix: 
        parts = line.strip().split()
        OPTAB[parts[0]] = parts[1]
    appendix.close()
    print("🚀 OPTAB was Loaded!")

def read_SYMTAB():
    sym = open("SymbolTable.txt", "r")
    for line in sym: 
        parts = line.strip().split() 
        SYMTAB[parts[0]] = parts[1]
    sym.close()
    print("🚀 SYMTAB was Loaded!")

def open_files():
    source = "intermideate.txt"
    dest = "output.obj"
    if len(sys.argv) > 2 : 
        source = sys.argv[1]
        dest = sys.argv[2]
    elif len(sys.argv) == 2 : 
        source = sys.argv[1]

    mdt = open(source,"r")
    listing_file = open("ListingFile.txt","w")
    obj = open(dest,"w")

    mdt.readline()
    mdt.readline()
    print("intermideate File is: ", source)
    print("object File is: ", dest)

    return mdt, listing_file, obj
    
def get_program_length():
    END = int(SYMTAB["END"],16)
    LEN = hex(END - LOCCTR)
    print("🚀 LOCCTR At : ",hex(LOCCTR))
    print("🚀 END At : ",hex(END))
    print("🚀 Program Lenght is: ",LEN)
    return LEN
