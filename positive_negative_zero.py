number = input('Enter the number')
if number.isnumeric():
  if int(number) == 0:
    print('Zero')
  elif int(number) > 0:
    print('Positive')
  else:
    print('Negative')
else:
  print('Invalid Input')
