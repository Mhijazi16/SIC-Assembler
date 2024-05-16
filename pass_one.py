# Made By Mohammed Hijazi
from typing import Dict
import sys

OPTAB: Dict[str,str] = {}
SYMTAB: Dict[str,str] = {}
LOCCTR = "" 
PRGNAME = ""
PRGLNGTH = ""

def open_symbol_table(): 
    global sym
    sym = open("SymbolTable.txt", "w")

def initialize_OPBTAB(): 
    with open("Appendix.txt","r") as appendix:
        for line in appendix : 
            n = line.strip().split()
            OPTAB[n[0]] = n[1]

def open_files(): 
    global code, dest, intmdt 
    if len(sys.argv) > 1: 
        source = sys.argv[1]
        dest = sys.argv[2]
        code = open(source, "r")
        intmdt = open(dest,"w")
    else:
        code = open("source.asm","r")
        intmdt = open("Intermediate.mdt","w")

def write_headers():
    global LOCCTR,PRGNAME
    intmdt.write("Line No.  Address         Source code             comments \n")
    intmdt.write("----------------------------------------------------------\n")

    first = code.readline()
    intmdt.write("                    ")
    intmdt.write("".join(first))
    one = first.strip().split()

    PRGNAME = one[0]
    LOCCTR = one[2]
    SYMTAB[one[1]] = one[2]
    sym.write(f"{one[1]} {one[2]} \n")
