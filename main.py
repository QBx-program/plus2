# Задача 1

my_list = [7, 5, 3, 3, 2]
reit = ''
while True:
    if not reit.isdigit():
        reit = input('Введите число: ')
    else:
        break
reit = int(reit)
my_list.reverse()
for i, num in enumerate(my_list):
    if num == reit:
        my_list.insert(i, reit)
        break
    if i == len(my_list) - 1:
        my_list.append(reit)
        break
my_list.reverse()
print(my_list)

