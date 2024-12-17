"""Advent of Code 2024 - Day 17 Part 1"""
from __future__ import annotations
import re
from dataclasses import dataclass
from math import trunc
from pathlib import Path


def parse_input(f_path: str = 'input.txt') -> tuple:
    patt = re.compile(r'Register \w\: (\d+)')
    inp = Path(f_path).read_text().split('\n\n')

    return list(map(int, patt.findall(inp[0]))), inp[1].split(' ')[1].strip()


@dataclass
class Registers:
    A: int
    B: int
    C: int


class Processor:

    def __init__(self, reg_vals: list[int]) -> None:
        self.registers = Registers(*reg_vals)
        self.ptr = 0

    def _get_combo_operand(self, oper: int) -> int:
        if oper in [0, 1, 2, 3, 7]:
            return oper

        if oper == 4:
            return self.registers.A
        elif oper == 5:
            return self.registers.B
        elif oper == 6:
            return self.registers.C

    def _instr0(self, oper: int) -> None:
        """instruction 0 - adv"""
        oper = self._get_combo_operand(oper)
        self.registers.A = trunc(self.registers.A / (2**oper))

    def _instr1(self, oper: int) -> None:
        """instruction 1 - bxl"""
        self.registers.B = self.registers.B ^ oper

    def _instr2(self, oper: int) -> None:
        """instruction 2 - bst"""
        self.registers.B = self._get_combo_operand(oper) % 8

    def _instr3(self, oper: int) -> None:
        """instruction 3 - jnz"""
        if self.registers.A != 0:
            self.ptr = oper - 2

    def _instr4(self, oper: int) -> None:
        """instruction 4 - bxc"""
        _ = oper
        self.registers.B = self.registers.B ^ self.registers.C

    def _instr5(self, oper: int) -> int | str:
        """instruction 5 - out"""
        return self._get_combo_operand(oper) % 8

    def _instr6(self, oper: int) -> None:
        """instruction 6 - bdv"""
        oper = self._get_combo_operand(oper)
        self.registers.B = trunc(self.registers.A / (2**oper))

    def _instr7(self, oper: int) -> None:
        """instruction 7 - cdv"""
        oper = self._get_combo_operand(oper)
        self.registers.C = trunc(self.registers.A / (2**oper))

    def run_program(self, pgm: str) -> int:
        pgm = list(map(int, pgm.split(',')))

        self.ptr = 0
        output = []
        while self.ptr < len(pgm) - 1:
            instr = pgm[self.ptr]
            operand = pgm[self.ptr+1]
            rtn = getattr(self, f'_instr{instr}')(operand)

            if rtn is not None:
                output.append(str(rtn))

            self.ptr += 2

        return ','.join(output)


if __name__ == '__main__':
    reg_vals, program = parse_input()

    proc = Processor(reg_vals)
    rtn = proc.run_program(program)

    print(f'Part 1 answer: {rtn}')
