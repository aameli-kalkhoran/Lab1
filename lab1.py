def age():
    try:
        age = int(input('Enter your age: '))
        print('Your age:', age)
    except ValueError:
        print('Please enter correct value.')

age()

