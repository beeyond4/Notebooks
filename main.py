#python3.10 main.py
import os


def notebooksprint(notebooks):
    print("\n"*32 + "\
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄\n\
█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█\n\
█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ --- Your notebooks --- ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█\n\
█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█\n\
████████████████████████████████████████████████████████████████████████████████████████\n\
█ {:<13} {:<70} █\
".format('Number','Name'))
    for dict in notebooks:
        num, name = dict["Num"], dict["Name"]
        print("█ {:<13} {:<70} █".format(num, name))
    print("\
█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n\
████████████████████████████████████████████████████████████████████████████████████████")


def tableprint(dicts, notebook_name): # Вывод ТАБЛИЦЫ в консоль
    strt = (76 - len(notebook_name))//2
    if (76 - len(notebook_name)) % 2 == 1: stp = strt + 1
    else: stp = strt
    print("\n"*32 + "\
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄\n\
█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█\n\
█" + "░" * strt + " --- " + notebook_name + " --- " + "░" * stp + "█\n\
█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█\n\
████████████████████████████████████████████████████████████████████████████████████████\n\
█ {:<3} {:<30} {:<6} {:<12} {:<15} {:<13} █\
".format('Num','Task','Time','Date','Status','Result'))
    for dict in dicts:
        num, task, time, date, status, result = dict.values()
        print("█ {:<3} {:<30} {:<6} {:<12} {:<15} {:<13} █".format(num, task, time, date, status, result))
    print("\
█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n\
████████████████████████████████████████████████████████████████████████████████████████")


def bottomfix(index):
    if index[:1] in '-0': return '1'
    return index


def notebooks_data():
    with open('DATA.csv', encoding='utf-8') as data:
        schedule_lst = list(map(lambda x: list(x.strip('\n').split(',')),data.readlines()))

#Наполняем НОВЫЙ список 'schedule' СЛОВАРЯМИ, со значениями из каждой строки
    schedule = []
    keys = ["Num","Name", "Path"]
    for String in schedule_lst:
        Dictionary = {}
        for index in range(len(keys)):
            Dictionary[keys[index]] = String[index]
        schedule.append(Dictionary)
    return schedule


def schedule_data(notebook): # Запись данных с ФАЙЛА 'notebook1.csv'

    # Считываем файл и сохраняем в СПИСОК
    with open("notebooks/" + notebook["Path"], encoding='utf-8') as data:
        schedule_lst = list(map(lambda x: list(x.strip('\n').split(',')),data.readlines()))

#Наполняем НОВЫЙ список 'schedule' СЛОВАРЯМИ, со значениями из каждой строки
    schedule = []
    keys = ["Num","Task","Time","Date","Status","Result"]
    for String in schedule_lst:
        Dictionary = {}
        for index in range(len(keys)):
            Dictionary[keys[index]] = String[index]
        schedule.append(Dictionary)
    return schedule


def notebook_create(number):
    tag = "notebook"+number+".csv"
    file = open("notebooks/"+tag, "w")
    file.close
    return tag


def byTASK(schedule):
    return schedule["Task"]


def byTIME(schedule):
    time = list(schedule["Time"].split('.'))
    return int(time[0]+time[1])


def byDATE(schedule):
    date = list(schedule["Date"].split('.'))
    return int(date[2]+date[1]+date[0])


def bySTATUS(schedule):
    if schedule["Status"] == "(Очень важно)":
        return 0
    elif schedule["Status"] == "(Важно)":
        return 1
    elif schedule["Status"] == "(Не важно)":
        return 2
    else: return 3


def byRESULT(schedule):
    if schedule["Result"] == "Не выполнено":
        return 0
    elif schedule["Result"] == "В процессе":
        return 1
    elif schedule["Result"] == "Выполнено":
        return 2
    else: return 3


def byAUTO(schedule):
    schedule.sort(key=byTASK)
    schedule.sort(key=byRESULT)
    schedule.sort(key=bySTATUS)
    schedule.sort(key=byTIME)
    schedule.sort(key=byDATE)
    return schedule


def Buffer(schedule):
    return schedule.pop(0)


def renumbering(schedule):
    for i in range(1, len(schedule)):
        schedule[i]["Num"] = str(i)
    return schedule


def notebook_remove(notebooks, index):
    os.remove("notebooks/"+notebooks[int(index)]["Path"])
    notebooks.pop(int(index))
    return notebooks


def schedule_remove(schedule, index):
    schedule.pop(int(index))
    return schedule


def notebook_edit(notebooks, index):
    name = input("\
███████████████████████████████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n\
█ Enter a new name of the notebook:  ░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n\
█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n\
█░░\═> \
    ")
    notebooks[int(index)]["Name"] = name
    return notebooks


def schedule_edit(schedule, index):
    change = list(input("\
███████████████████████████████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n\
█ Enter <column>, <new parameter>:   ░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n\
█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n\
█░░\═> \
").split(', '))
    if change[0] == "Num":
        schedule.insert(int(change[1]), schedule.pop(int(index)))
    else:
        schedule[int(index)][change[0]] = change[1]
    return schedule


def notebook_add(notebooks, move):
    name = input("\
███████████████████████████████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n\
█ Enter a name for the new notebook: ░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n\
█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n\
█░░\═> \
")
    if len(move) == 2 and move[1] == '~':
        pathname = "1"
        move.pop(1)
    else: pathname = str(int(notebooks[-1]["Path"][8:-4])+1)
    new_notebook = {
    "Num" : "0",
    "Name" : name,
    "Path" : notebook_create(pathname)
    }
    del pathname #delete pathname
    notebooks.append(new_notebook)
    return notebooks


def schedule_add(schedule): # Добавление заметки
    note = input("\
███████████████████████████████████████████████████████████████████████████░░░░░░░░░░░░░\n\
█ Enter note (RU):                                                       ░█░░░░░░░░░░░░░\n\
█ <Num>, <Task>, <minutes.seconds>, <day.month.year>, <Status>, <Result> ░█░░░░░░░░░░░░░\n\
█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█░░░░░░░░░░░░░\n\
█░░\═> ")
    note = list(note.split(', '))
    note[0] = bottomfix(note[0])
    note[4]=str('(' + note[4] + ')')
    #List to Dict
    keys = ["Num","Task","Time","Date","Status","Result"]
    notice = {}
    for i in range(len(keys)):
        notice[keys[i]] = note[i]
    schedule.insert(int(note[0]), notice)
    return schedule


def schedule_write(schedule, notebook):
    if notebook["Path"] == "DATA.csv": path = "DATA.csv"
    else: path = "notebooks/" + notebook["Path"]
    with open(path, 'w', encoding='utf-8') as String:
        for k in schedule:
            lst=[]
            for i in k:
                lst.append(k[i])
            String.write(','.join(lst)  + '\n')


def schedule_sort(schedule):
    lock = input("\
███████████████████████████████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n\
█ 1 ══ By Task                       ░█░░░░░░░░░░░░░░░░░░   /\…/\        ░░░░░░░░░░░░░░░\n\
█ 2 ══ By Date - Time                ░█░░░░░░░░░░░░░░░░░   (‘•.•’)        ░░░░░░░░░░░░░░\n\
█ 3 ══ By Status                     ░█░░░░░░░░░░░░░░░░░   ..=*=..        ░░░░░░░░░░░░░░\n\
█ 4 ══ By Result                     ░█░░░░░░░░░░░░░░░░░  (.\.||./.)~~**  ░░░░░░░░░░░░░░\n\
█ 0 ══ Auto                          ░█░░░░░░░░░░░░░░░░░░                ░░░░░░░░░░░░░░░\n\
█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n\
█░░\═> \
")
    buffer = Buffer(schedule)
    if lock == '1': schedule.sort(key=byTASK)
    elif lock == '2':
        schedule.sort(key=byTIME)
        schedule.sort(key=byDATE)
    elif lock == '3': schedule.sort(key=bySTATUS)
    elif lock == '4': schedule.sort(key=byRESULT)
    else: schedule = byAUTO(schedule)
    schedule.insert(0, buffer)
    return schedule


def notebook_action(schedule):
    if len(notebooks) == 1:
        move = list(input("\
█ Type <+> to create a notebook:     ░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n\
█ Type <L> to Leave:                 ░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n\
█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n\
█░░\═> \
").split(' '))
        move.append('~')
    else:
        move = list(input("\
█ Enter action:                      ░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n\
█ O ══ Open notebook <Number>        ░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n\
█ + ══ Create notebook               ░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n\
█ ~ ══ Rename notebook <Number>      ░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n\
█ - ══ Delete notebook <Number>      ░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n\
█ L ══ Leave                         ░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n\
█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n\
█░░\═> \
").split(' '))
    return move


def schedule_action(schedule):
    if len(schedule) == 1:
            path = list(input("\
█ Type <+> to create a note:         ░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n\
█ Type <C> to close this notebook:   ░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n\
█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n\
█░░\═> \
").split(' '))
    else: path = list(input("\
█ Enter action:                      ░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n\
█ + ══ Add note                      ░█░░░░░░░░░░░░░░░░░░░░  /\_/\ ♥ ░░░░░░░░░░░░░░░░░░░\n\
█ ~ ══ Edit <Number>                 ░█░░░░░░░░░░░░░░░░░░░  > ^,^ <   ░░░░░░░░░░░░░░░░░░\n\
█ - ══ Delete <Number>               ░█░░░░░░░░░░░░░░░░░░░    / \     ░░░░░░░░░░░░░░░░░░\n\
█ ! ══ Sort                          ░█░░░░░░░░░░░░░░░░░░░    (__)__  ░░░░░░░░░░░░░░░░░░\n\
█ D ══ Clear notebook                ░█░░░░░░░░░░░░░░░░░░░░          ░░░░░░░░░░░░░░░░░░░\n\
█ C ══ Close notebook                ░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n\
█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n\
█░░\═> \
").split(' '))
    return path


def DANGER():
    print("Action entered incorrectly, please try again")

# Блок работы приложения
null = {
"Num" : "|",
"Task" : "|",
"Time" : "|",
"Date" : "|",
"Status" : "|",
"Result" : "|"
}
nullN = {
"Num" : "|",
"Name" : "|",
"Path" : "|"
}

while True:
    notebooks = notebooks_data()
    notebooks.insert(0, nullN)
    notebooksprint(notebooks)
    move = notebook_action(notebooks)
    if len(move) == 2 and move[1] != '~': move[1] = bottomfix(move[1])
    if move[0] in 'OОоo0ЩщJj': notebook = notebooks[int(move[1])]["Path"]
    elif move[0] in '+=': notebooks = notebook_add(notebooks, move)
    elif move[0] in '~`ёЁ': notebooks = notebook_edit(notebooks, move[1])
    elif move[0] in '-_': notebooks = notebook_remove(notebooks, move[1])
    elif move[0] in 'LlДд': break
    else:
        DANGER()
        continue

# Entering notebook*
# -------------------
    while move[0] == 'O':
        schedule = schedule_data(notebooks[int(move[1])])
        schedule.insert(0, null)
        tableprint(schedule, notebooks[int(move[1])]["Name"])
        path = schedule_action(schedule)
        if len(path) == 2: path[1] = bottomfix(path[1])
        if path[0] in "+=": schedule = schedule_add(schedule)
        elif path[0] in "~`ёЁ": schedule = schedule_edit(schedule, path[1])
        elif path[0] in "-_": schedule = schedule_remove(schedule, path[1])
        elif path[0] in "!1": schedule = schedule_sort(schedule)
        elif path[0] in 'DdВв': schedule = [{}]
        elif path[0] in 'CСcс': break
        else:
            DANGER()
            continue
        schedule = renumbering(schedule)
        schedule.pop(0)
        schedule_write(schedule, notebooks[int(move[1])])
# -------------------

    notebooks = renumbering(notebooks)
    notebooks.pop(0)
    schedule_write(notebooks, {"Path" : "DATA.csv"})

# END

print("\n" * 32 + "Goodbye) \n\n\
@@@  @@@@@@@   @@@@@@@@@@   @@@@@@@@               @@@    @@@  @@@@@@@\n\
@@@  @@@@@@@@  @@@@@@@@@@@  @@@@@@@@              @@@@   @@@@  @@@@@@@@\n\
@@!  @@!  @@@  @@! @@! @@!       @@!             @@@!!  @@@!!  @@!  @@@\n\
!@!  !@   @!@  !@! !@! !@!      !@!                !@!    !@!  !@   @!@\n\
!!@  @!@!@!@   @!! !!@ @!@     @!!    @!@!@!@!@    @!@    @!@  @!@!@!@\n\
!!!  !!!@!!!!  !@!   ! !@!    !!!     !!!@!@!!!    !@!    !@!  !!!@!!!!\n\
!!:  !!:  !!!  !!:     !!:   !!:                   !!:    !!:  !!:  !!!\n\
:!:  :!:  !:!  :!:     :!:  :!:                    :!:    :!:  :!:  !:!\n\
 ::   :: ::::  :::     ::    ::                    :::    :::   :: ::::\n\
:    :: : ::    :      :    : :                     ::     ::  :: : ::"\
+ "\n" * 14)
