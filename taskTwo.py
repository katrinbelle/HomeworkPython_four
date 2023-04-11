#  В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.
numberBushes=int(input("Введите количество кустарников-> "))
import random
numberBurries=[]
maxNumberBurries=int(0)
if numberBushes==0:
    print("Эх, тогда ничего собрать не получиться, раз нет кустарников")
else:    
    for i in range(numberBushes):   #рандомное кол ягод
        numberBurries.append(random.randint(0,21))
    print("Количество ягод на каждом кусте равно=", end='')
    print(*numberBurries,sep=', ' )
    if numberBushes>3:
        for i in range(len(numberBurries)):   #поиск максимального кол
            if i==0:
                temp=numberBurries[i]+numberBurries[i+1]+numberBurries[len(numberBurries)-1]
            elif  i==len(numberBurries)-1:
                temp=numberBurries[i]+numberBurries[i-1]+numberBurries[i-len(numberBurries)-1]
            else:
                temp=numberBurries[i-1]+numberBurries[i]+numberBurries[i+1]
            if temp>maxNumberBurries:
                maxNumberBurries=temp
    else:
        for i in range(len(numberBurries)):
            maxNumberBurries+=numberBurries[i]

    print(f"Количество ягодов , которое можно собрать максимально равно= {maxNumberBurries}")