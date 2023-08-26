numero = -9999
contador = 0
soma = 0

while numero != 999:
    numero = int(input('Digite um valor inteiro (999 para parar): '))
    if numero == 999:
        break
    else:
        soma += numero
        contador +=1
print(f'Foram inseridos {contador} números e a soma deles é {soma}!')