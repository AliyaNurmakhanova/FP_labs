# 1. Тізімдерді, кортеждерді, жиындарды және сөздіктерді бір бағдарламаның ішінде көрсететін бағдарлама жаз.
# Мәлеметтер ретінде әр студент өзіне байланысты ақпарат немесе резюмесін ұсыну қажет.
lists = ['Nurmakhanova', 'Aliya']
tuples = ('Almaty', '20')
sets = {'functional programming', 'mobile programming', 'application design patterns'}
dictionaries = {'university': 'SU', 'speciality': 'computer science'}
print(lists)
print(tuples)
print(sets)
print(dictionaries)

# 2. Тізімдердегі, кортеждердегі, жиындардағы және сөздіктердегі әдістерді қарастырып,
# барлығына ортақ 5 әдісті және ерекшеленетін бірнеше (2-3) әдістерді қолдананатын бағдарлама жаз.
listsSec = ['Jeon', 'Jungkokok']
tuplesSec = ('Seoul', '25')
setsSec = {'singing', 'dancing', 'rapping'}
dictionariesSec = {'entertainment': 'Hybe', 'label': 'BigHit'}

print(lists + listsSec)
print(tuples + tuplesSec)

print(len(sets))
print(len(dictionaries))

print(min(lists))
print(min(tuples))

print(max(sets))
print(max(dictionaries))

print(tuples.count('Almaty'))

lists.extend(listsSec)
print(lists)
print(lists.reverse())
print(lists.clear())

print(tuples.count('Almaty'))

sets.discard('functional programming')
print(sets)
sets.update(setsSec)
print(sets)

print(dictionaries.items())
print(dictionaries.get("university"))