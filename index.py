x = 'hello'
y = 'world'
a = 1
b = 2

def helloWorld():
    print(x + ' ' + y)
    print(a + b)

helloWorld()

def fizzBuzz(number):
    if number % 15 == 0:
        print('fizzBuzz')
    elif number % 5 == 0:
        print('buzz')
    elif number % 3 == 0:
        print('fizz')
    else:
        print(number)

fizzBuzz(30)

people = ['andy', 'gabriel', 'meghan']

people.pop(0)
people.append('luke')

for name in people:
    print(name)