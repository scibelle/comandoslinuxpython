# -*- coding: utf-8 -*-
"""
Created on Mon May 29 18:51:00 2017

@author: alunoufc
"""
import os;

comando = raw_input("Digite o comando que deseja executar: ")

if(comando=='ls'):
    os.system("ls");
if(comando=='mkdir'):
    b=raw_input("Digite o diretorio que deseja criar: ");
    os.system("mkdir "+b);
    
