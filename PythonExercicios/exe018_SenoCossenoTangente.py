from math import radians,sin, cos, tan
angulo = float(input('Digite o ângulo que você deseja: '))
print('O ângulo de {:.2f} tem o SENO de {:.2f}'.format(angulo, sin(radians(angulo))))
print('O ângulo de {:.2f} tem o COSSENO de {:.2f}'.format(angulo, cos(radians(angulo))))
print('O ângulo de {:.2f} tem o TANGENTE de {:.2f}'.format(angulo, tan(radians(angulo))))