from time import sleep

#Class
#Syntaxa
class Computador:
    '''param marca: Recebe a Marca do computador.
    param memoria: Recebe a Memória RAM do computador.
    param placavideo: Recebe a Placa de Vídeo do computador.
    '''
    def __init__(self, marca, memoria, placavideo):
        self.marca = marca
        self.memoria = memoria
        self.placavideo = placavideo

    def ligar(self):
        print('Estou ligando...')

    def desligar(self):
        print('Estou desligando...')

    def processandooperacoes(self):
        print('Processando informações solicitadas...')
        sleep(2)
    
    def imprimirconfiguracao(self):
        print(f'Minha Marca é: {self.marca}', end=' ') 
        print(f'possuo Memória Ram de: {self.memoria}', end=' ')
        print('e placa de vídeo: {self.placavideo}')
