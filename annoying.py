while True:
    print('Enter your age: ')
    age = input()
    if age.isdecimal():
        break
    print('Please enter a valid number.')
while True:
    print('Enter new password: ')
    password = input()
    if password.isalnum():
        break
    print('Please enter alphanumeric only.')