largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
area = largura * altura
print('Sua parade tem a dimensão de {:.2f}X{:.2f} e sua área é de {:.3f}m².'.format(largura, altura, area))
print('Para pintar essa parede, você precisará de {:.3f}l de tinta.'.format(area/2))