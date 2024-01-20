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
    ['r3', 'ABT8I78', 110.98, 100, 'comum'],
    ['r3', 'multarx', 107.00, 100, 'comum'],
    ['r3', 'multary', 102.00, 101, 'comum']

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

    velApurada = registroVeiculo[i][2]
    
    velPermitida = (registroVeiculo[i][3] + 7) if registroVeiculo[i][3] <=100 else registroVeiculo[i][3]
    
    placa = registroVeiculo[i][1]
    codRadar = registroVeiculo[i][0]
    tipoVeiculo = registroVeiculo[i][4]
    pctExcesso = (float(velApurada) - float(velPermitida))/float(velPermitida) * 100

    if (tipoVeiculo == "comum") and \
       (pctExcesso > 0):
                       #and 
       #((velPermitida<=100) and (velApurada>(velPermitida+7))) : 
        print(f"{placa}   -  {pctExcesso  :.2f}   -  {codRadar}")
