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

def pass_one():
    global LOCCTR
    index = 1
    for line in code:
        i = 0 
        n = line.strip().split()
        
        if not n : 
            continue
        if n[i] !='.':

            intmdt.write(f"{index}          ")
            intmdt.write(hex(int(LOCCTR,16)) + "      ")
            intmdt.write("".join(line))
            
            if n[i] not in OPTAB.keys() and n[i] != '-':
                current = hex(int(LOCCTR,16))
                SYMTAB[n[i]] = str(current)
                sym.write(f"{n[i]} {current} \n")
                i += 1


            if n[i] in OPTAB.keys() or n[i]=="WORD":
                current = hex(int(LOCCTR,16)+3)
                LOCCTR = str(current)
            elif n[i]=="BYTE":
                if n[i+1][0]=="X":
                    size = int((len(n[i+1])-3)/2)
                    current = hex(int(LOCCTR,16)+size)
                    LOCCTR = str(current)
                elif n[i+1][0]=="C":
                    size = (len(n[i+1])-3)
                    current = hex(int(LOCCTR,16)+size)
                    LOCCTR = str(current)
            elif n[i]=="RESW":
                words = int(n[i+1],16) * 3 
                current = hex(int(LOCCTR,16)+words)
                LOCCTR = str(current)
            elif n[i]=="RESB":
                size = int(n[i+1])
                current = hex(int(LOCCTR,16)+size)
                LOCCTR = str(current)
            index += 1
