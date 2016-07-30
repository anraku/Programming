import sys

if __name__ == '__main__':
  param = sys.argv

  A = int(param[1])
  K = int(param[2])
  target = 2*(10**12)
  money = A
  day = 0

  if(K is 0):
    day = target - money
    print (day)
    sys.exit()

  while money < target:
    money += 1+money*K
    day += 1

  print(day)