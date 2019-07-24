### Level 1: Minion Task
counts = dict()
data = list(input('Input Test Data: '))

n = int(input('Input n here: '))

def answer(data, n):
    new_list = list()
    for number in data:
        counts[number] = counts.get(number, 0) + 1  
    for key, values in counts.items():
        if values <= n:
            try:
                key = int(key)
            except:
                continue
            new_list.append(key)
        else:
            continue
    print(new_list)
