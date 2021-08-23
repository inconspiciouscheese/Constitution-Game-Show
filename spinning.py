import time
import os

def spinning():
  os.system("clear")
  print("\u001b[1000D◐\nSpinning")
  time.sleep(.5)
  os.system("clear")
  print("\u001b[1000D◓\nSpinning.")
  time.sleep(.5)
  os.system("clear")
  print("\u001b[1000D◑\nSpinning..")
  time.sleep(.5)
  os.system("clear")
  print("\u001b[1000D◒\nSpinning...")
  time.sleep(.5)
  os.system("clear")
 
for i in range(4):
  spinning()


print("That would be way too many. Imagine trying to fit that many people in one room. And it would be so \u001b[3mloud\u001b[0m.. Adams shudders at the thought.")