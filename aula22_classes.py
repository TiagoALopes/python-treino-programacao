from entity.Computador import Computador

try:
    marca = input('Digite a Marca do computador: ')
    memoria = input('Digite a Memória do computador: ')
    placavideo = input('Digite a Plava de Vídeo do computador: ')
    
    computador1 =  Computador(marca, memoria, placavideo)
    computador1.ligar()
    computador1.processandooperacoes()
    computador1.imprimirconfiguracao()
    computador1.desligar()
except(Exception):
    print('Por gentileza informar um valor válido.')

