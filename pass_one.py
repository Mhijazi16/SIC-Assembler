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

