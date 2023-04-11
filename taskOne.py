# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
def chekData(litsData,sample,numberList): #проверка на количество
        if len(litsData)!=sample[numberList]:
            return 1 
def inputDate(listNumber,listNumbers,number):   #проверка вводных данных
    flag=True
    messeng=''
    ferst='первого'
    if number==1:
         ferst='второго'
    while flag:
        listNumber=input(f'Введите {messeng} числа для {ferst} списка->    ')
        listNumber=list(map(int,listNumber.split()))
        if chekData(listNumber,listNumbers,number)!=1:
            messeng='повторно'
            flag=False
    return listNumber
def add(list,str): #преобразует в лист
    for x in str:
          list.append(x)
    return list
def listMany(m,list):  #преобразует в множество
    for x in list:
          m.add(x)
    return m
def sorting(x):  #сортировка
    if len(x)==1:
        return x
    elif len(x)==0:
        return 0
    else:
        for i in range(0,len(x)):
            for j in range(0,len(x)):
                 if x[i] <x[j]:
                    temp=x[i]
                    x[i]=x[j]
                    x[j]=temp
        return x       
manyFerst=set() 
manySecond=set()
union=[]   
colRows=input('Введите количество чисел для первого и для второго списка ->    ')
listNumber=list(map(int,(colRows.split())))
numbersFerst=''
numbersSecond=''
numbersFerst=inputDate(numbersFerst,listNumber,0)
numbersSecond=inputDate(numbersSecond,listNumber,1)
listUnion=list(map(int,(add(union,(listMany(manyFerst,numbersFerst).intersection(listMany(manySecond,numbersSecond)))))))
if not listUnion:
     print('В обоих наборах одинаковые числа не встречаются')
else:
    print('В обоих наборах встречаются числа ->',end='')
    print(*(sorting(listUnion)))