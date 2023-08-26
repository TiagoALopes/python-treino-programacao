frase = ' Curso em vídeo python '
print(frase[3])
print(frase[0:15:2])
print(frase)
print(frase.strip()) #Funciona como o trim em C# e Java.
print(frase.strip().replace('python','Android')) #Funciona como o trim em C# e Java.
print('Quantidade de O:',frase.upper().count('O'))
print('Curso' in frase)
print(frase.strip().find('vídeo'))
divido = frase.split()
print('A primeira sub-lista é {}'.format(divido[2]))
print(''' Textão ''')