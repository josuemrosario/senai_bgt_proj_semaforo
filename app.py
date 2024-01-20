#  r1        BEE4R22   70.00         60         comum
#  r1        DKR5Y21   67.00         60      especial
#  r1        ABX4I22   60.00         60         comum
#  r1        ABT8I78   67.01         60         comum
#  r2        VXX0f74   56.90         80         comum
#  r2        AKR7T45   87.00         80         comum
#  r2        ADD1G78   89.90         80         comum
#  r2        CFG3J77   73.89         80         comum
#  r3        ERR3J79   73.89        100         comum
#  r3        ERP1J22   65.89        100         comum
#  r3        BNG9J99  110.89        100      especial
#  r3        ABT8I78  110.98        100         comum



registroVeiculo = [
    ['r1', 'BEE4R22', 70.00, 60, 'comum'],
    ['r1', 'DKR5Y21', 67.00, 60, 'especial'],
    ['r1', 'ABX4I22', 60.00, 60, 'comum'],
    ['r1', 'ABT8I78', 67.01, 60, 'comum'],
    ['r2', 'VXX0f74', 56.90, 80, 'comum'],
    ['r2', 'AKR7T45', 87.00, 80, 'comum'],
    ['r2', 'ADD1G78', 89.90, 80, 'comum'],
    ['r2', 'CFG3J77', 73.89, 80, 'comum'],
    ['r3', 'ERR3J79', 73.89, 100, 'comum'],
    ['r3', 'ERP1J22', 65.89, 100, 'comum'],
    ['r3', 'BNG9J99', 110.89, 100, 'especial'],
    ['r3', 'ABT8I78', 110.98, 100, 'comum']

]
#print(registroVeiculo[0][2])




#placa = 'ADD1G78'
#pctExcesso = 12.37
#codRadar = 'r2'
#veiculoEspecial = False


#Porcentagem_excesso = [(vel_auf - vel_perm)/vel_perm] * 100

# registroVeiculo.len()
# for elemento in registroVeiculo

print("PLACA   - PCT      - RADAR")

#print(dir(registroVeiculo))
# print(type(registroVeiculo))
# print(registroVeiculo.__len__())


for i in range(0,len(registroVeiculo)):
    pctExcesso = (float(registroVeiculo[i][2]) - float(registroVeiculo[i][3]))/float(registroVeiculo[i][3]) * 100
    if registroVeiculo[i][4] == "comum" and pctExcesso > 0  : #veiculoEspecial == False
        print(f"{registroVeiculo[i][1]}   -  {pctExcesso  :.2f}   -  {registroVeiculo[i][0]}")
