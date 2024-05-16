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
