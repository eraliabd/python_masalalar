Erali Dev 
Sana: 21-05-2022

Masala: S = 1^N+2^(N-1)+3(N-2)+...+N^1
Yechimi: Python dasturlash tilida.

n = int(input("n ni kiriting: "))
s = 0
for i, j in zip((list(range(-n, 0))), list(range(1, n + 1))):
    s += pow(j, -i)
print(s)
