#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: aesteban

"""
import sys


class Calculadora():
    def plus(self, op1, op2):
         
         return op1 + op2
         
    def minus(self, op1, op2):
         
         return op1 - op2

Mi_Calcu = Calculadora()

if __name__ == "__main__":
    try:
        operando1 = int(sys.argv[1])
        operando2 = int(sys.argv[3])
    except ValueError:
        sys.exit("Error: Non numerical parameters")

    if sys.argv[2] == "suma":    
        result = Mi_Calcu.plus(operando1,operando2)
    elif sys.argv[2] == "resta":
        result = Mi_Calcu.minus(operando1,operando2)
    else:
        sys.exit('Operación sólo puede ser sumar o restar.')

    print(result)