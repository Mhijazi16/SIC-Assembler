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

def handle_directives(parts,index):
    if not listing_file:
        return 

    opcode = parts[index]
    if opcode == "RESW"  :
        listing_file.write("\n")
        return 
    elif opcode == "RESB":
        listing_file.write("\n")
    elif opcode == "RSUB": 
        listing_file.write("4C0000\n")
        CODE.append("4C0000")
        return
    elif opcode == "BYTE":
        operand = parts[index+1]
        val = operand[2:len(operand)-1]
        if operand.find("X") != -1:
            listing_file.write(f"{val} \n")
            CODE.append(val)
        elif operand.find("C") != -1:
            tmp = ""
            for c in val: 
                hexa = str(hex(ord(c)))
                tmp += hexa[2:]
            listing_file.write(f"{tmp} \n")
            CODE.append(tmp)
    elif opcode == "WORD":
        operand = str(hex(int(parts[index+1])))        
        operand = operand[2:]
        if len(operand) < 6:
            operand = extend_number(operand,6)
        listing_file.write(f"{operand} \n")
        CODE.append(operand)


def handle_indexed(opcode,operand):
    if not listing_file: 
        return 

    code = OPTAB[opcode]
    address = int(SYMTAB[operand],16)
    address += 2**15
    hexa = hex(address)[2:]
    code += hexa
    listing_file.write(code)
    CODE.append(code)

def handle_direct(opcode,operand):
    if not listing_file: 
        return 

    code = OPTAB[opcode]
    code += SYMTAB[operand][2:]

    listing_file.write(code)
    CODE.append(code)

    
def write_instruction(line:str): 

    parts = line.strip().split()
    if parts[0] == '.':
        return 

    flag = False
    if len(parts) <= 5: 
        line = line.strip()
        while len(line) != 50: 
            line += " "
        listing_file.write(line)
    else:
        flag = True

    index = 0
    while parts[index] not in OPTAB.keys() and parts[index] not in DIREC:  
        index += 1
        if index == len(parts) and "END" not in parts: 
            print(f"⚠️ WARNING!! line :{parts[0]} Does not have Opcode or Directive")
            return 
        if index == len(parts):
            return
    opcode = parts[index]

    if flag: 
        line = line.strip().split(parts[index+2])[0]
        while len(line) != 50: 
            line += " "
        listing_file.write(line)

    if opcode in DIREC:
        handle_directives(parts,index)
        return

    operand = parts[index+1]
    if operand not in SYMTAB.keys():
        x = operand.find(",")
        if  x == -1 or operand[:x] not in SYMTAB.keys(): 
            print(f"⚠️ WARNING!! line :{parts[0]}. SYMBOL: {parts[index+1]} is Not Defined")
            return


    if operand.find(",") != -1 :
        handle_indexed(opcode,operand[:len(operand)-1])
    else :
        handle_direct(opcode,operand)
        
    listing_file.write("\n")

def to_hex(x): 
    return hex(x)[2:]
def to_dec(x): 
    return int(x,16)
def write_headers(): 

    listing_file = open("ListingFile.txt","r")
    listing_file.readline()
    TMP = ""
    LOCCTR2 = int(SYMTAB["START"],16)
    for line in listing_file: 

        parts = line.strip().split()
        LOCCTR = int(parts[1],16)
        X = LOCCTR - LOCCTR2

        if X + 3 > 30 or parts[len(parts)-1] not in CODE or "RESB" in parts or "RESW" in parts: 
            obj.write(f"T^{extend_number(hex(LOCCTR2)[2:],6)}^{hex(X)[2:]}{extend_number(TMP,6)}\n")
            while "RESW" in parts or "RESB" in parts: 
                line = listing_file.readline()
                parts = line.strip().split()
                LOCCTR = int(parts[1],16)

            LOCCTR2 = LOCCTR
            TMP = ""


        TMP += f"^{parts[len(parts)-1]}"
    obj.write(f"E^{extend_number(SYMTAB['START'],6)}")





mdt, listing_file, obj = open_files()
read_OPTAB()
read_SYMTAB()
LOCCTR = int(SYMTAB["START"], 16)
PRGLGTH = get_program_length()
PRGNAME = read_program_name()

for line in mdt:
    write_instruction(line)
listing_file.close()

write_headers()
mdt.close()
# Made By Mohammed Hijazi
