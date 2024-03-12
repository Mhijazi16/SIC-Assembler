
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
