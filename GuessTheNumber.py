import time
from random import seed
from random import randint

seed(1)
for _ in range(10):
    value = randint(1, 100000)
def guess123():
      print ('''
Type (exit) To Exit!
Type (num) To See The Number!
                                                   ''')
      x = input('Enter a number from 1 until 100000: ')
      x=int(x)
      if x == value:
          print ('Congratulations You Find It!')
          print (value)
          time.sleep(3)
          z = input('Do you want to play again [y/n]: ')
          if z == 'y':
               guess123()
          elif z == 'n':
               exit()
          else:
               print ('Wrong Option!')
               time.sleep(2)
               exit() 

      elif x < value:
          print ("Higher (+)")
          guess123()

      elif x > value:
          print ("Lower (-)")
          guess123()
        
      elif x == "num":
          print (num)
          time.sleep(1)
          guess123()
      elif x == "exit":
          exit()

guess123()
