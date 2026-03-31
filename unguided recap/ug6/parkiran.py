n = int(input())
yesterday = input()
today = input()

count = 0
for i in range(n):
    if yesterday[i] == today[i] == 'M':
        count = count + 1

print(count)