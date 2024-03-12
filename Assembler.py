
from functools import partial
from typing import Dict, List


class Instruction: 
    def __init__(self,Label,Opcode,Operand,Comment) -> None:
        self.Label = Label
        self.Opcode = Opcode
        self.Operand = Operand
        self.Comment = Comment
    def __str__(self) -> str:
        return f"{self.Label} {self.Opcode} {self.Operand} {self.Comment}"

class Assembler: 
    def __init__(self) -> None:
        self.LOCCTR = 0
        self.PRGLTH = 0 
        self.PRGNAME = ""
        self.SYBTAB: Dict[str,Instruction] = {}
        self.OPTAB: Dict[str,str] = {}
        self.Code: Dict[str,Instruction] = {}

        with open("Appendix.txt") as appendix: 
            for line in appendix:
                parts = line.strip().split()
                self.OPTAB[parts[0]] = parts[1]

    def getInstruction(self,line : str) -> Instruction:
        return Instruction(line[0:10],line[11:20],line[22:39],line[40:70]) 

    def pass_one(self):
        pass
    def pass_two(self):
        pass 


