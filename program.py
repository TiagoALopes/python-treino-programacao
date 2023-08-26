from datetime import date

print("Welcome to the greeter program")
name = input("Enter your name: ")
parsecs = input("Enter your parsecs: ")
lightyears = 3.26 * float(parsecs)
print("Greetings " + name + ' ' + str(parsecs) + ' parsecs equivale a ' + str(lightyears) + ' lightyears')
print('Greetings', name, parsecs, 'parsecs equivale a ', lightyears, ' lightyears')
print('Greetings {0}! {1} parsecs equivale a {2} lightyears'.format(name, parsecs, lightyears))

