import sys

def Part_1()
  filename = sys.argv[-1]
  with open(filename) as f: lines = [int(i.strip()) for i in f.readlines()]

  x = 0
  y = 0
  for l in lines:
    cmd = l.split(" ")

    if cmd[0] == "forward":
      x += int(cmd[1])
    elif cmd[0] == "up":
      y -= int(cmd[1])
    elif cmd[0] == "down"
      y += int(cmd[1])
    
  return x * y



def solve():
  print(Part_1)



solve()
