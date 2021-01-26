goods = []
features = {'название': '', 'цена': '', 'количество': '', 'единица измерения': ''}
analytics = {'название': [], 'цена': [], 'количество': [], 'единица измерения': []}
x = 0
while True:
    if input('Для выхода нажмите "q", для прололжения "Enter": ').upper() == 'Q':
        break
    x += 1
    features = features.copy()
    for f in features:
        pro = input(f'Введите значение "{f}": ')
        features[f] = int(pro) if f == 'цена' or f == 'количество' else pro
        analytics[f].append(features[f])
    goods.append((x, features))
    print(f"Структура товаров:{goods}")
    print(f'Текущая аналитика по товарам:')
    for key, value in analytics.items():
        print(f'{key:>30}: {value}')
