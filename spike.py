import time, sys

try:
  while True:
    for i in range(1,20):
      print('-' * i)
      time.sleep(0.1)
    for i in range(20,1,-1):
      print('-' * i)
      time.sleep(0.1)
except KeyboardInterrupt:
  sys.exit()