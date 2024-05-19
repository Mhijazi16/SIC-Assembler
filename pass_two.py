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

def read_program_name():

    line = mdt.readline()
    listing_file.write(f"{line}")

    parts = line.strip().split()

    if parts[0] not in OPTAB.keys():
        obj.write(f"H^{parts[0]}^{extend_number(hex(LOCCTR)[2:],6)}^{extend_number(PRGLGTH[2:],6)}\n")
        print("🚀 Program Name is: ", parts[0])
        return parts[0]
    obj.write(f"H^{PRGNAME}^{hex(LOCCTR)[2:]}^{PRGLGTH[2:]}\n")
    return ""

def extend_number(number:str,extent): 
    if len(number) >= extent:
        return number
    while len(number) != extent:
        number = "0" + number
    return number

def subtract(one,two):
    one = int(one,16)
    two = int(two,16)
    return hex(one - two)
