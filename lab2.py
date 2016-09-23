arr = [12,6,8]

#Минимальный элемент массива
def Min(arr):
    cont = arr[0]
    for i in arr:
        if i < cont:
            cont = i
    print("Наименьший элемент массива:", cont)
Min(arr)    

#Среднее арифметическое
def Arif(arr):
    buf = 0
    c = len(arr)
    for i in arr:
        buf +=i
    buf /=c
    print("Среднее арифметическое = ", buf)
    
Arif(arr)
    
hw = "Hello World"

#Реверс строки
def Swap(hw):
    print(hw)
    wh = list(hw)
    wh.reverse()
    print(''.join(wh))

Swap(hw)

