file = open('text.txt', 'r')
text = file.read()
print(text)
file.close()

file = open('text.txt', 'r')
line = file.readline()
print(line)
file.close()

file = open('text.txt', 'r')
word = file.read(4)
print(word + '\n')
file.close()

file = open('text.txt', 'r')
line = file.__next__()
nextLine = file.__next__()
print(line + '\n' + nextLine)
file.close()