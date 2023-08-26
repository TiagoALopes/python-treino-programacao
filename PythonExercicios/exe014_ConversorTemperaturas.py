celcius = float(input('Informe a temperatura em °C: '))
fahrenheit =  celcius * (9/5) + 32
kelvin = celcius + 273.15
print('A temperatura de {:.1f} °C corresponde a {:.1f} °F e {:.1f} K!'.format(celcius, fahrenheit, kelvin))