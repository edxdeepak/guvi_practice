try:
  number = int(input('Enter the number'))
  if number % 2 == 0:
    print('Even')
  else:
    print('Odd')
except:
  print('Invalid Input')
