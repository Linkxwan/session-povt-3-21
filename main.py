from catalog import catalogue


def catalog():
    print('-' * 50)
    print('-Каталог товаров:')
    for name, price in catalogue.items():
        print('---- {0:20} цена: {1} сом'.format(name, price))
    print('-' * 50)


def check():
    try:
        budget = int(input('-Ваш бюджет = '))
    except Exception:
        print('Введите бюджет, ничего лишнего!')
    finally:
        catalog()
        while True:
            search = str(input('-Поиск товаров: '))
            if search == 'выход':
                print('До свиданья, приходите в наш магазин есще!')
                break
            if search in catalogue:
                item = catalogue[search]
                if budget > item:
                    budget -= item
                    print(f'---Вы купили {search} за {item} сом')
                    print(f'---Ваш баланс: {budget} сом')
                else:
                    print('У вас не достаточно средств, пополните баланс!')
            else:
                print('---Увы... Такого товара нету на складе....')


def main():
    check()

if __name__ == '__main__':
    main()
