import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of program')

def factorial(num):
  logging.debug('Start of factorial')
  total = 1
  for i in range(1, num + 1):
    total *= i
    logging.debug('i is ' + str(i) + ', total is ' + str(total))
  logging.debug('End of factorial(' + str(num) +')')
  return total

print(factorial(5))