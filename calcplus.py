#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
@author: aesteban
"""
import sys

from calcoohija import CalculadoraHija
    
Mi_Calcu = CalculadoraHija()

fich = open(sys.argv[1],'r')
lista = fich.readlines()# lista con todas las lineas
fich.close()

for linea in lista:
    
    elemento = linea.split(',') # Con SPLIT troceamos la cadena con el argumento que queramos, en este caso ","
    elemento[-1] = elemento [-1][:-1]
    operacion = elemento[0]
    
    operandos = elemento[1:]
    op_aux = int()
    
    if operacion == 'suma':
        op_aux = 0
        
        for op_final in operandos :  
            result1 = Mi_Calcu.plus(op_aux,int(op_final))
            op_aux = result1
        
        print ('El resultado de la suma es: ' + str(result1))
        
    elif operacion == 'resta':
        op_aux = int(operandos[0])
        
        for op_final in operandos[1:]:  
            result2 = Mi_Calcu.minus(op_aux,int(op_final))
            op_aux = result2
            
        print ('El resultado de la resta es: ' + str(result2))   
         
    elif operacion == 'multiplica':
        op_aux = 1
        
        for op_final in operandos :  
            result3 = Mi_Calcu.mult(op_aux,int(op_final))
            op_aux = result3
        
        print ('El resultado de la division es: ' + str(result3)) 
       
    elif operacion == 'divide':
        op_aux = int(operandos[0])
        
        for op_final in operandos[1:]:  
         
            result4 = Mi_Calcu.div(op_aux,int(op_final))
            op_aux = result4

        print ('El resultado de la division es: ' + str(int(result4))) 
    
    else:
        sys.exit('ERROR')
        
        
        
        
   
