import random
import time


def step2_no_umbrella():
    print(
        'Как только утка-маляр вышла из дома начался ливень. '
        'Соответственно ей пришлось бежать до ближайшего бара.'
    )
    time.sleep(2)
    bar_types = ['Red Socks', 'Mephist', 'Blue Rabbit']
    bar_type = random.choice(bar_types)
    print(f'Ближайшим баром оказался: \"{bar_type}\".')
    print('Для того, чтобы высохнуть и согреться '
          'ей пришлось изрядно выпить спиртного.')
    time.sleep(2)
    drinks = ['Long Island', 'Aperol', 'Jägermeister', 'Absent']
    for i in range(6):
        print(f'{i + 1} коктейль - {random.choice(drinks)}')
        time.sleep(1)
    print('Стоит ли еще расслабиться после тяжелого дня и плохой погоды?')
    operation = ''
    while operation not in ['да', 'нет']:
        print('Выберите: да/нет.')
        operation = input()
    if operation == 'да':
        print('Главный герой решился опустошить фирменный '
              f'коктейль в баре \"{bar_type}\".')
        time.sleep(2)
        if bar_type == 'Mephist':
            print(
                'Утка выпила \"Ядерный\" коктейль. '
                'После чего танцевала в баре круче всех '
                'и забрала премию за лучший танец ночи.'
            )
        elif bar_type == 'Red Socks':
            print(
                'Утка выпила коктейль \"Красный Чепушила\". '
                'И весьма разбушевалась в баре, пытаясь со всеми подраться. '
                'Поэтому пришлось вызвать сотрудников и отправить в полицию. '
            )
        else:
            print(
                'Утка выпила коктейль \"Славная Охота\". '
                'Он оказался слишком сильным для утки. '
                'Поэтому утка-маляр моментально уснула прям в баре. '
            )
        time.sleep(2)
        print('В конечном счете у утки была насыщенная ночь и '
              'с утра большую часть она не помнила.')
    else:
        time.sleep(2)
        print('Утка так и ушла домой, не совершив никаких приключений.')
    return


def step2_umbrella():
    print(
        'На всякий случай утка взяла зонт и тем самым не прогадала. '
        'Поэтому даже в плохую погодy утка-маляр '
        'решила дойти до приличного бара.'
    )
    time.sleep(1)
    for i in range(5):
        print(i + 1)
        time.sleep(1)
    print('Придя в бар, она решила перекусить '
          'и слегка выпить приличного алкоголя.')
    time.sleep(2)
    drinks = ['Prosecco', 'Martini', 'Арарата']
    meals = ['Стейк Рибай', 'Запеченый дорадо с овощами', 'Пиццу']
    print(f'Ее выбор пал на {random.choice(meals)}. '
          f'Выпить она взяла немного {random.choice(drinks)}.')
    time.sleep(2)
    print('Спокойно поужинав в прекрасном месте, '
          'она собралась и пошла, любуясь красотами города.')
    return


def step1():
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()
    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()


if __name__ == '__main__':
    step1()
