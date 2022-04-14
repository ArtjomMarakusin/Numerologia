def readDictVal(dic: dict)->list: ## считывает значения из словарей
    mas = []
    for v in dic.values():
        mas.append(v.strip(''))
    return mas

def readDictKeys(dic: dict)->list: ## считывает ключи из словарей
    mas = []
    for v in dic.keys():
        mas.append(v.strip(''))
    return mas

def getNameNumber(numb: list, lett: list, name: str): ## производится вычисление числа имени и дальнейший вывод в соответствующее окно
    name_list = list(name)
    name_numbers = 0
    n = 0
    sum = 0
    for i in name_list:
        l = name_list[n]
        index = lett.index(l)
        numbers = numb[index]
        sum += int(numbers)
        n += 1

    sum1 = 0
    sum2 = 0
    sum3 = 0
    k = 0

    if sum < 10:
        text = f"Число имени - {sum}"
    elif sum >= 10:
        sum1 = sum % 10
        sum2 = sum // 10
        sum3 = sum1 + sum2
        if sum3 < 10:
            text = f"Число вашего имени - {sum3}"
        elif sum3 >= 10:
            a = sum3 // 10
            b = sum3 % 10
            k = a + b
            text = f"Число вашего имени - {k}"
    return text
