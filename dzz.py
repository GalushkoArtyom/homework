running=True
hours=1
while running:
    studydays = int(input('input valid amount of days'))
    if studydays<0 and studydays>7:
        print('input valid amount of days')
        break
    if studydays==1:
        hours = float(input('введите кол-во часов в 1 день'))
    if studydays==2:
        hours = float(input('введите кол-во часов в 1 день'))
        hours = float(input('введите кол-во часов в 2 день'))
    if studydays==3:
        hours = float(input('введите кол-во часов в 1 день'))
        hours = float(input('введите кол-во часов в 2 день'))
        hours = float(input('введите кол-во часов в 3 день'))
    if studydays==4:
        hours = float(input('введите кол-во часов в 1 день'))
        hours = float(input('введите кол-во часов в 2 день'))
        hours = float(input('введите кол-во часов в 3 день'))
        hours = float(input('введите кол-во часов в 4 день'))
    if studydays==5:
        hours = float(input('введите кол-во часов в 1 день'))
        hours = float(input('введите кол-во часов в 2 день'))
        hours = float(input('введите кол-во часов в 3 день'))
        hours = float(input('введите кол-во часов в 4 день'))
        hours = float(input('введите кол-во часов в 5 день'))
    if studydays==6:
        hours = float(input('введите кол-во часов в 1 день'))
        hours = float(input('введите кол-во часов в 2 день'))
        hours = float(input('введите кол-во часов в 3 день'))
        hours = float(input('введите кол-во часов в 4 день'))
        hours = float(input('введите кол-во часов в 5 день'))
        hours = float(input('введите кол-во часов в 6 день'))
    if studydays==7:
        hours = float(input('введите кол-во часов в 1 день'))
        hours = float(input('введите кол-во часов в 2 день'))
        hours = float(input('введите кол-во часов в 3 день'))
        hours = float(input('введите кол-во часов в 4 день'))
        hours = float(input('введите кол-во часов в 5 день'))
        hours = float(input('введите кол-во часов в 6 день'))
        hours = float(input('введите кол-во часов в 7 день'))
    while hours<=0:
        print(input('Введите кореектное число часов учебы в день'))
