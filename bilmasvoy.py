"""Masala sharti:
Bilmasvoy matematika darsida
Bilmasvoy matematika darsida sondan 1 ni ayirishni o’rgangan edi. U darsdan chiqib uyga borgancha o’qituvchisi o’rgatgan ba’zi narsalar yodidan ko’tarildi. 
Shundan so’ng u o’zining sondan 1 ni ayirish algoritmini o’ylab topdi. Uning fikricha sondan 1 ni ayirish quyidagicha bajariladi:

Agar sonning oxirgi raqami 0 ga teng bo’lmasa shu son 1 taga kamaytiriladi
Agar sonning oxirgi raqami 0 ga teng bo’lsa shunchaki sonning oxirgi raqami o’chiriladi. 
(10 ga bo’lgan kabi, ya’ni 1000 soni 100 ga o’zgaradi, son 0 bo’lganda o’zgarmaydi).

Kiruvchi ma'lumotlar:
Kirish faylining yagona satrida ikkita butun son,N(2≤N≤10^9) va K(1≤K≤50) sonlari kiritiladi.

Chiquvchi ma'lumotlar:
Chiqish faylida Bilmasvoy o’z algoritmi yordamida N sonidan K marotaba 1 ni ayirganida hosil bo’ladigan natijani chop eting!

Yechimi:"""
n,k=map(int,input().split())
i=1
while i<=k:
    if n%10!=0:
        n=n-1
    elif n%10==0:
        n=n//10
    i+=1
print(n)
