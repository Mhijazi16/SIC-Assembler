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
