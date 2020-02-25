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

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = str(age)
        self.gender = gender
    
    def whoIAm(self):
        print("hello, my name is" + ", " + self.name + ", " + "and I am a" + " " + self.age + "-year-old" + " " + self.gender + ".")

firstPerson = Person('luke', 39, 'male')
firstPerson.whoIAm()

def repLetters(string):
    repString = ''
    for letter in string:
        letter += letter
        repString += letter
    return repString

print(repLetters('dude'))