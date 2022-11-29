permissions = {}
n = int(input())
for _ in range(n):
    s = input().split()
    permissions[s[0]] = set(s[1:])
for _ in range(int(input())):
        perm, file = input().split()
        if perm == 'read':
            perm = 'R'
        if perm == 'write':
            perm = 'W'
        if perm == 'execute':
            perm = 'X'
        if perm in permissions[file]:
            print('OK')
        else:
            print('Access denied')

# section = []
# for i in range(5):
#     member = input().split(',')
#     section.append(member)
#
# for i in range(5):
#     for j in range(i+1, 5):
#         if int(section[i][0]) > int(section[j][0]):
#             section[i], section[j] = section[j], section[i]
#
# print(section)