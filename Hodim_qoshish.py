#Muallif: Abdinazarov Erali 19/12/2021
#Hodimni ro'yxatga olish tizimi

kirit = "....... HODIMLAR RO'YXATI .......\n"
kirit += ">>> Hodimlar ro'yxatini ko'rish uchun 1 ni bosing\n"
kirit += ">>> Hodim kiritish uchun 2 ni bosing\n"
kirit += ">>> Tizimdan chiqish uchun (q) ni bosing\n>>>"

hodim1 = {
    'ism':'Alijon',
   'familiya':'Valiyev',
   'lavozim':'Dasturchi',
   'oylik':'$1200'}

hodim2 = {
    'ism':'Valijon',
   'familiya':'Aliyev',
   'lavozim':'Dasturchi',
   'oylik':'$1000'}
hodimlar = [hodim1,hodim2]

while True:
    qiymat = input(kirit)
    if qiymat == '1':
        print("\n---- Hodimlar ro'yxati ----")
        for info in hodimlar:
            print(f"Ismi: {info['ism']}\nFamiliyasi: {info['familiya']}\n"
                  f"Lavozimi: {info['lavozim']}\nOyligi: {info['oylik']}\n")
            print("................................\n")
        menyu = "Bosh bo'limga qaytish uchun 0 ni bosing\n>>>"
        print(input(menyu))
        if menyu == '0':
            continue
    if qiymat == 'q':
        break

    if qiymat == '2':
        print("----Yangi hodim qo'shish")
        hodim = {}
        hodim['ism'] = input("Hodimning ismi >>> ")
        hodim['familiya'] = input("Hodimning familiyasi >>> ")
        hodim['lavozim'] = input("Hodimning lavozimi >>> ")
        hodim['oylik'] = input("Hodimning oyligi >>> ")
        hodimlar.append(hodim)
        print("Muvaffaqiyatli qo'shildi!")
        print(input(menyu))
        
        
        