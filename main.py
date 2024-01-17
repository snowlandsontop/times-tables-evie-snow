#ask the user for a number
num = int(input("Pick a positive number: "))

#initialize counter
count = 0

#multiply the number by the numbers 0 through 10
while (count <= 10):
  print(str(count) + "*" + str(num) + "=" + str(count*num))
  count = count + 1