
# VERİ TİPLERİ (DATA TYPES)

# NUMBERS (and TYPES)

yas = 29
print(yas)
#29

# integer = 5 tam sayılar
# float   = 5,56 ondalıklı sayılar
# long    = 5565656565L uzun sayılar
# complex = 3,14j karmaşık sayılar

# Python hesapmakinesi gibi kullanılabilir:
# toplama:
print(15+15)
#30
# strings de toplanabilir:
print("gökay" + ".com")
#gökay.com

# çıkarma:
print(15-15)
#0
print(-15-(-8))
#-7

# çarpma: 
print(15*15)
#225
# strings de çarpılabilir:
print("adım "*2,"geliyor at.")
#adım adım  geliyor at.

# bölme:
print(15/15)
#1.0

# mod alma, modülüs (yüzde işareti ile yapılır):
print(40 % 8)
#0  (40'ın 8'e bölümünde kalan 0 (sıfır)'dır.)
# modülüs sonucu kalanı verir.

# küp alma - kare alma (üslü sayılar):
print(4 ** 3) # 3 ile küp alır. 4*4*4 olarak görür.
#64
print(4 ** 2) # 2 ile karesini alır. 4*4 olarak görür.
#16

# noktalı sonuçların noktasını atarak hesaplama:
print(40 // 6)
#6
# 40'ın 6'ya bölümü 6,6666666 olarak sonuçlandığı halde, // işareti ile virgül-
# den sonrasını atarak sadece baştaki sayıyı yazdırdı. Bu, yuvarlama anlamına
# gelmez. Python'da yuvarlama round() ile yapılır:
print(round(40 / 6))
#7

