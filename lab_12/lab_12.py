# Файлмен жұмыс жасауды үйрену.
# Минимум 5 операция жасайтын ауқымды бағдарлама құру.
firstFile = open('smth.txt', 'w')

while True:
    i = input("Введите элемент: ")
    if i == ' ' or i == '':
        break
    firstFile.writelines(str(i) + '\n')

firstFile.close()

firstLst = []
secondFile = open('smth.txt', 'r')

while True:
    line = secondFile.readline()
    if not line:
        break
    firstLst.append(int(line.strip()))
print(firstLst)

secondLst = []
for i in firstLst:
    secondLst.append(pow(i, 2))
print(secondLst)

secondFile.close()
