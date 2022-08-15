h, m, s = map(int, input().split())
new_s = int(input())
s += new_s
m += s // 60
s %= 60
h += m // 60
m %= 60
h %= 24

print(h, m, s)