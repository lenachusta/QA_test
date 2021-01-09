import json
import datetime

# открытие файла
with open("todos.json") as response:
    todos = json.load(response)


# определение завершенных и оставшихся задач
def complited(id, bool):
    complited_tasks = []
    for task in todos:
        try:
            if task["userId"] == id:
                if task["completed"] == bool:
                    if len(task["title"]) > 50:
                        complited_tasks.append(f'{task["title"][:50]}...')
                    else:
                        complited_tasks.append(task["title"])
        except:
            pass
    return complited_tasks


# создание списка пользователей
users_id = []
for user in todos:
    try:
        users_id.append(user["userId"])
    except:
        pass
for i in users_id:
    for j in users_id:
        if users_id[i] == users_id[j]:
            users_id.remove(users_id[j])

# дата и время для названия и файла
date1 = datetime.datetime.today().strftime("%Y-%m-%d")
date2 = datetime.datetime.today().strftime("%d.%m.%Y")
time1 = datetime.datetime.today().strftime("%H-%M")
time2 = datetime.datetime.today().strftime("%H:%M")

# создание и заполнение файлов
for id in users_id:
    f = open(str(id) + '_' + str(date1) + 'T' + str(time1) + '.txt', 'w')
    f.write('# Сотрудник №' + str(id))
    f.write('\n' + str(date2) + ' ' + str(time2) + '\n')
    f.write('\n## Завершённые задачи:\n')
    f.writelines("%s\n" % i for i in complited(id, True))
    f.write('\n## Оставшиеся задачи:\n')
    f.writelines("%s\n" % i for i in complited(id, False))
    f.close()

