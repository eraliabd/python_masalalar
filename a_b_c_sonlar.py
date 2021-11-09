# -*- coding: utf-8 -*-
"""
@Muallif: Erali Abdinazarov 09/11/2021
"""

a,b,c=list(map(int, input().split()))

if c>a and c>b and b>a:
    print(f"{a}<{b}<{c}")
elif b>c and b<a and a>c: 
    d=a 
    a=c
    c=d
    print(f"{a}<{b}<{c}")
elif a>b and a<c and b<c:
    k=a
    a=b
    b=k
    print(f"{a}<{b}<{c}")
elif a==b and a<c and b<c:
    print(f"{a}≤{b}<{c}")
elif a==c and a<b and b>c:
    m=b
    b=c
    c=m
    print(f"{a}≤{b}<{c}")
elif a>b and a>c and b==c:
    n=a
    a=c
    c=n
    print(f"{a}≤{b}<{c}")