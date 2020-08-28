import random 
r = random.randint(1,50)

while True:
  x = input ('請猜猜看1到50的整數')
  x = int(x)
  if x == r :
   print ('你猜對了')
   break
  elif x > r :
      print ('比答案大')
  elif x < r:
      print('比答案小')	