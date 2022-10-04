#  1. Кіші және бас әріптерді қамтитын жол енгізіледі.
#  Бір жағдайда бірдей жолды шығару қажет, ол қай әріптердің үлкенірек екеніне байланысты.
#  Егер тең болса, кіші әріпке түрлендіріңіз. Мысалы, «HeLLo World» жолы енгізілсе, оны «hello world» түрлендіру керек,
#  себебі бастапқы жолда кіші әріптер көбірек. Кодыңызда for циклды пайдаланыңыз. upper() (бас әріпті түрлендіру) және
#  lower () (кіші әріпті түрлендіру), сонымен қатар жолдың немесе
#  таңбаның регистрін тексеретін isupper() және islower() әдістері.
"""string = "Hello World"
upper = 0; lower = 0
for i in string:
    if i.isupper():
        upper += 1
    else:
        lower += 1
if upper > lower:
    print(string.upper())
else:
    print(string.lower())"""

# 2. isdigit() жол әдісі жолда тек сандар бар-жоғын тексереді. Енгізуден екі бүтін санды сұрайтын және
# олардың қосындысын басып шығаратын программа жазыңыз. Қате енгізілген жағдайда, бағдарлама қатемен аяқталмауы керек,
# бірақ сандарды сұрауды жалғастыру керек. try-exception ерекше жағдай өңдеушісін пайдаланылмауы керек.
"""a = input("a = ")
b = input("b = ")
while not(a.isdigit() and b.isdigit()):
    print("Input number!")
    a = input("a = ")
    b = input("b = ")
print(int(a) + int(b))"""

# Минимум 10 жолдарға арналған функциялар мен әдістерді қолданып бағларлама жазып шық.
x = 'laboratory'
y = '444'
print(x + y)
print(x * 3, y * 3)
print('len x =', len(x), 'and len y =', len(y))
print(x[5], 'and', y[1])
print(x[1:7], 'and', y[::-1])
print(x.isalpha(), 'and', y.isalpha())
print(x.islower(), 'and', y.islower())
print(x.isupper(), 'and', y.isupper())
print(x.isdigit(), 'and', y.isdigit())
print(x.isnumeric(), 'and', y.isnumeric())
print(x.startswith('lab'), 'and', y.startswith('lab'))
print(x.endswith('444'), 'and', y.endswith('444'))
print(x.upper(), 'and', y.upper())
print(x.find('a', 2, 7), 'and', y.find('4'))
print(x.replace('o', '#'), 'and', y.replace('4', '5'))
print(x.join('work'), 'and', y.join('labs'))