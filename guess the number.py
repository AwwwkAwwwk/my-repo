import random

number = random.randint(1, 100)

user_number = None
count = 0
levels = {1: 10, 2: 7, 3: 5}

level = int(input('Выберите уровень сложности от 1 до 3: '))
max_count = levels[level]
print('У вас', max_count, 'попыток!')

user_count = int(input('Введите количество игроков: '))
users = []
for i in range(user_count):
    user_name = input(f'Введите имя пользователя {i + 1} :')
    users.append(user_name)
print(users)

is_winner = False
winner_name = None
while not is_winner:
    count += 1
    if count > max_count:
        print('Все проиграли :(')
        break
    print(f'Попытка № {count}')
    for user in users:
        print(f'Ход игрока {user}')
        user_number = int(input('Угадайте число от 1 до 100: '))
        if user_number == number:
            is_winner = True
            winner_name = user
            break

        elif number < user_number:
            print('Ваше число БОЛЬШЕ, попробуй еще.')
        else:
            print('Ваше число МЕНЬШЕ, попробуй еще.')
else:
    print(f'Победитель {winner_name}!')
