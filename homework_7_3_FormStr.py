# Использование старого метода:
team1_num = 5
team2_num = 6

print("В команде Мастера кода участников: %s!" % team1_num)
print("Итого сегодня в командах участников: %s и %d!" % (team1_num, team2_num))

# Использование format():
score_2 = 42
team1_time = 18015.2

print("Команда Волшебники данных решила задач: {}!".format(score_2))
print("Волшебники данных решили задачи за {} с!".format(team1_time))

# Использование f-строк:
score1 = 40
score2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = score1 + score2
time_avg = (team1_time + team2_time)/tasks_total

if score1 > score2 or score1 == score2 and team1_time > team2_time:
    challenge_result = 'Победа команды Мастера кода!'
elif score1 < score2 or score1 == score2 and team1_time < team2_time:
    challenge_result = 'Победа команды Волшебники данных!'
else:
    challenge_result = 'Ничья!'

print(f"Команда Волшебники данных решила задач: {score2} !")
print(f"Волшебники данных решили задачи за {team1_time} с !")
print(f"Команды решили {score1} и {score2} задач.")
print(f"Результат битвы: {challenge_result}")
print(f"Сегодня было решено {tasks_total} задач, в среднем по {round((time_avg), 1)} секунды на задачу.")