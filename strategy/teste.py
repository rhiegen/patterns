from statistics import mode
from typing import List
import re





ovr = 'STEP.DDNAME DD UNIT=(SYSDA,30),DATACLAS=XDEFAULT,STORCLAS=EXTNOST3'
indice = ovr.find('DD ')
string = ovr[indice+3:]

# Three digit number followed by space followed by two digit number
pattern_unit_simple = '(UNIT=SYSDA)'
pattern_unit_number = '(UNIT=\(SYSDA\,)(\d+)(\))'  # None if not found
pattern_dataclas='(DATACLAS=)(\w+)'
pattern_storclas='(STORCLAS=)(\w+)'

# match variable contains a Match object.
match_unit_simple = re.search(pattern_unit_simple, string) 
match_unit_number = re.search(pattern_unit_number, string) 
match_dataclas = re.search(pattern_dataclas, string) 
match_storclas = re.search(pattern_storclas, string) 

if match_dataclas != None:
    dataclas = match_dataclas.group()
if match_storclas != None:
    storclas = match_storclas.group()
if match_unit_number != None:
    unit = match_unit_number.group()
if match_unit_simple:
    unit = match_unit_simple.group()

print(f'unit {unit} dataclas {dataclas} storclas {storclas}')

