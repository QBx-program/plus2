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

# Задача 2

db = []
analiz_db = {}
product = []
price = []
quantity = []
unit = []
i = 0

def add_product(i):
    product = input('Введите наименование товара ')
    price = input('Введите цену товара ')
    quantity = input('Введите количество товара ')
    unit = input('Введите ед.измерения ')
    new_product = [i, {'Название:': product, 'Цена:': price, 'Количество:': quantity, 'Ед.изм.:': unit}]
    return new_product


while True:
    still = input('Добавить товар? (д/н) ')
    if still == 'д' or still == 'Д':
        i += 1
        db.append(tuple(add_product(i)))
    if still == 'н' or still == 'Н':
        break

for n, prod in enumerate(db):
    product.append(db[n][1]['Название:'])
    price.append(db[n][1]['Цена:'])
    quantity.append(db[n][1]['Количество:'])
    unit.append(db[n][1]['Ед.изм.:'])

analiz_db = {'Название:': set(product), 'Цена:': set(price), 'Количество:': set(quantity), 'Ед.изм.:': set(unit)}

print(analiz_db)

print(db)
