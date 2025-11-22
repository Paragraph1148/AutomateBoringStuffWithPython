import sys
def collatz(num):
  if num <= 0:
    raise ValueError("Collatz is defined for positive integers only")
  if num == 1:
    return
  elif num % 2 == 0:
    num = num // 2
    print(num, end=' ')
    return collatz(num)
  else:
    num = 3 * num + 1
    print(num, end=' ')
    return collatz(num)
while True:
  try:
    number = int(input('Enter number'))
    if number <= 0:
      raise ValueError
    break
  except ValueError:
    print('Please enter positive integer value only.')
  except KeyboardInterrupt:
    sys.exit()
collatz(number)
print()