import random

EXPERIMENTS = 10000
count = 0

def has_six_streak(seq):
  streak = 1
  for i in range(1, len(seq)):
    if seq[i] == seq[i-1]:
      streak += 1
      if streak == 6:
        return True
    else:
      streak = 1
  return False

for _ in range(EXPERIMENTS):
  flips = [random.choice(['H', 'T']) for _ in range(100)]
  if has_six_streak(flips):
    count += 1

print(float(count)/EXPERIMENTS*100)