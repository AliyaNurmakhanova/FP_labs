# Nurmakhanova Aliya
# FP lab-3
# 1. Екі бүтін А және В саны берілген (А ≤ B бар). А-дан В-ға дейінгі барлық сандарды басып шығарыңыз.

# A = int(input("A-ны еңгізіңіз: "))  # а-ны консольда еңгіземіз
# B = int(input("B-ны еңгізіңіз: "))  # b-ны консольда еңгіземіз

# for ab in range(A, B + 1):          # for циклы арқылы A дан B ға дейін шығару керектігі туралы диапазон қоямыз,
#     # B кірмегендіктен + 1 қосамыз
#     print(ab, end=' ')              # сосын print арқылы пробелмен шығарамыз


# 2. А және В екі бүтін сандар берілген. А<B болса, өсу ретімен немесе басқаша жағдайда кему ретімен
# А-дан В-ға дейінгі барлық сандарды басып шығарыңыз.
# if A < B:                  # шарт қоямыз, А дан B үлкен болса, өсу ретімен
#     for ab in range(A, B + 1):
#         print(ab, end=' ')
# else:                             # болмаса, яғни A дан B кіші болса, кему ретімен
#     for ab in range(A, B - 1, -1):
#         print(ab, end=' ')


#  3. Екі бүтін А және В саны берілген, A>B. А-дан В-ға дейінгі барлық тақ сандарды
#  кему ретімен басып шығарыңыз. Бұл тапсырмада if операторынсыз орындай аласыз.
# for ab in range(A - (A + 1) % 2, B - B % 2, -2):
#     print(ab, end=' ')


# 4. Үстел ойыны үшін 1-ден N-ге дейінгі сандары бар карталар пайдаланылады. Бір карта жоғалады.
# Қалған карталардың сандарын білу арқылы оны табыңыз.
# N саны берілген, содан кейін N − 1 қалған карталардың саны (1-ден N-ге дейінгі әртүрлі сандар).
# Бағдарлама жоғалған картаның нөмірін көрсетуі керек.
lost = 0     # бос мән
n = int(input("Карталар саны: "))
for i in range(1, n + 1):       # сумма всех карт
    lost += i
for i in range(n - 1):          # бір карта жоғалады
    lost -= int(input("Қалған карта номері: "))        # Қалған карталарды белгілейміз
print("Жоғалған картаның номері", lost)             # жоғалған картанын номерін шығарамыз