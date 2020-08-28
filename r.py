import random 
r = random.randint(1,50)
count = 0
while True:
  count = count + 1	
  x = input ('請猜猜看1到50的整數')
  x = int(x)
  if x == r :
      print ('你猜對了')
      print('這是你猜的第', count , '次')
      break
  elif x > r :
      print ('比答案大耶')
  elif x < r:
      print('比答案小')	
  print('這是你猜的第', count , '次')