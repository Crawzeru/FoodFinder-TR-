


# Yemek tarifleri ve malzemeler
yemek_tarifleri = {
    "Spagetti": ["makarna", "domates sosu", "sucuk"],
    "Omlet": ["yumurta", "peynir", "biber", "domates"],
    "Sandviç": ["ekmek", "salatalık", "domates", "peynir"],
    "Mantı":["un","su","tuz","yumurta","kıyma","kuru soğan","domates salçası","tereyağ"],
    "Pişi":["yumurta","yoğurt","tuz","kabartma tozu","un","yağ"],
    "Sütlaç":["pirinç","su","süt","şeker","nişasta",],
    "Tavuk Göğsü":["süt","toz","şeker","tereyağı","pirinç unu","nişasta","vanilin","tavuk göğsü"],

}

# Malzemeleri kullanıcıdan al
malzemeler = input("Yan yana malzemeleri girin (virgülle ayırın): ").split(",")

# Hangi yemeğin yapılabilir olduğunu kontrol et
uygun_yemekler = []
for yemek, tarif_malzemeleri in yemek_tarifleri.items():
    if all(malzeme.strip() in tarif_malzemeleri for malzeme in malzemeler):
        uygun_yemekler.append(yemek)

# Sonuçları yazdır
if uygun_yemekler:
    print("Bu malzemelerle yapabileceğiniz yemekler:\n-", "\n- ".join(uygun_yemekler))
else:
    print("Bugün aç kaldın,dışardan söyle!")

