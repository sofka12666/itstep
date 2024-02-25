numbersList = []

number = 1

while number != 0:

   number = int(input("Введіть число "))

   numbersList.append(number)

sum = 0

for i in numbersList:

   sum += i

middle = (sum / len(numbersList)) * 100 / 100

print(f"Середнє значення = {middle}")