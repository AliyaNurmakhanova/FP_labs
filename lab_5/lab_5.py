# 1. Бағдарламалау секцияларына қатысатын әртүрлі топтағы студенттерді таныстыруды сұрайтын бағдарламаны жазыңыз.
# Тізімді сыныптардың өсу реті бойынша сұрыптау қажет. Фамилиялар мен сыныптардың тізімін басып шығарыңыз.
# name = ["Sam", "Ann", "Daniel", "Jungkook", "Christopher"]
# course = ["C++", "Java", "Dart", "Python", "C"]
# print("name: ", name)
# name.sort()
# print("sorted name: ", name)
# print("courses: ", course)
# course.sort()
# print("sorted courses: ", course)

# 2. Тізім қайтаратын функция жазып шығу. Алдын ала студенттердің пәндері және бағалары бар тізім құрастыр.
# Және сол тізім бойынша студенттің атын еңгізген кезде, сол студенттің бағаларын шығарып бертін болсын.
a = [["Jungkook", 91],
     ["Christopher", 90]]
name = input("name: ")
for i in range(len(a)):
    for j in range(len(a)):
        if name == a[i][0]:
            print(a[i][0], ": ", a[i][1])
            break
        else:
            print("Ondai student joq!")
            break

# 3. Пайдаланушыға бүтін мәндерді сұрайтын және оларды тізім ретінде сақтайтын бағдарламаны жазыңыз.
# Мәндерді енгізудің аяқталуының көрсеткіші ретінде нөлді пайдалану керек. Содан кейін бағдарлама пайдаланушы енгізген
# барлық сандарды (нөлден басқа) өсу ретімен көрсетуі керек - әр жолға бір мән.
# Сұрыптау үшін sort әдісін немесе sorted функцияны пайдаланыңыз.
# list = []
# while True:
#     n = int(input('number = '))
#     list += [n]
#     if n == 0:
#         break
# print(sorted(list, reverse=True))

# students' resume
# resume = ["Aliya", "Nurmakhanova", "7074459335", "SU", "Computer scince"]
# print("Last name:", resume[0], "\nName:", resume[1], "\nPhone:", resume[2],
#       "\nUniversity:", resume[3], "\nSpeciality:", resume[4])
#
# resume.append(20)
# print("\n", resume)
#
# x = "7751218313"
# resume.insert(2, x)
# print("\n", resume)
#
# resume.pop(3)
# print("\n", resume)
#
# resume.reverse()
# print("\n", resume)