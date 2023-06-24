# random modülü nedir ?

# Python programlama dilinin standart kütüphanesinde yer alan bir modüldür. 
# Bu modül, rastgele sayı üretimi, rastgele seçimler yapma, rastgele örnekleme yapma ve diğer rastgele işlemleri gerçekleştirmek için bir dizi işlev sağlar.

import random # ile sayfaya dahil edilir.


# 1  - random()                                 : 0 ile 1 arasında rastgele bir ondalık sayı döndürür.

for i in range(10):
    print(random.random())              # her çalştığında farklı farklı 0 ile 1 arası rastgele ondalıklı sayılar döndürür.


# 2  - betavariate(alpha, beta)                 : Beta dağılımına göre rastgele bir ondalık sayı döndürür.

# 3  - choice(seq)                              : Verilen bir diziden rastgele bir öğe seçer.

liste = ["siyah","kırmızı","mavi","sarı","beyaz",3,4,5]
print(random.choice(liste))                          # listeden rastgele eleman döner


# 4  - choices(population, weights=None, k=1)   : Verilen bir popülasyondan, ağırlıklarla desteklenen şekilde rastgele öğeler seçer.
# 5  - expovariate(lambd)                       : Lambda parametresine sahip bir üstel dağılıma göre rastgele bir ondalık sayı döndürür.
# 6  - gammavariate(alpha, beta)                : Gamma dağılımına göre rastgele bir ondalık sayı döndürür.
# 7  - gauss(mu, sigma)                         : Normal (Gauss) dağılıma göre rastgele bir ondalık sayı döndürür.
# 8  - getrandbits(k)                           : K bitlik rastgele bir tamsayı döndürür.

# 9  - getstate()                               : Rastgele sayı üreteci durumunu döndürür.

# Rastgele sayı üretimindeki durumu elde etmek için getstate() kullanımı
state = random.getstate()
print("Durum:", state)

# Durum geri yüklendiğinde aynı rastgele sayılar üretilebilir
random.setstate(state)

# Durum geri yüklendikten sonra rastgele bir sayı üretme
random_number = random.randint(1, 100)
print("Rastgele Sayı:", random_number)

# 10 - lognormvariate(mu, sigma)                : Log-normal dağılıma göre rastgele bir ondalık sayı döndürür.
# 11 - normalvariate(mu, sigma)                 : Normal (Gauss) dağılıma göre rastgele bir ondalık sayı döndürür.
# 12 - paretovariate(alpha)                     : Paretto dağılımına göre rastgele bir ondalık sayı döndürür.
# 13 - randbytes(n)                             : N bayt uzunluğunda rastgele bir bayt dizisi döndürür.

# 14 - randint(a, b)                            : Belirtilen aralıkta (a ve b dahil) rastgele bir tamsayı döndürür.

for i in range(5):
    print(random.randint(3,5))          # 3 ile 5 (3 ile 5 dahil) arasında rastgele integer değerler döner.


# 15 - randrange(start, stop[, step])           : Belirtilen aralıkta rastgele bir tamsayı döndürür.

for i in range(5):
    print(random.randrange(1,9,2))      # 1 ile 6 sınırları arasında (üst sınır dahil değil)2 şer atlayarak integer değerler döner.


# 16 - sample(population, k)                    : Bir popülasyondan, belirtilen sayıda rastgele öğeleri seçer.

# 17 - seed(a=None, version=2)                  : Rastgele sayı üretecinin başlangıç durumunu ayarlar.

# 18 - setstate(state)                          : Rastgele sayı üreteci durumunu ayarlar.

# 19 - shuffle(seq)                             : Bir dizinin öğelerini rastgele sıralar.

liste = ["siyah","kırmızı","mavi","sarı","beyaz",3,4,5]
random.shuffle(liste)
print(liste)                            # / [4, 'kırmızı', 'mavi', 3, 'beyaz', 'siyah', 'sarı', 5]
print(liste)                            # / [3, 'mavi', 5, 'kırmızı', 'sarı', 4, 'siyah', 'beyaz']


# 20 - triangular(low, high, mode)              : Üçgensel bir dağılıma göre rastgele bir ondalık sayı döndürür.

# 21 - uniform(a, b)                            : Belirtilen aralıkta rastgele bir ondalık sayı döndürür.

for i in range(10):
    print(random.uniform(3,7))          # 3 ile 7 arasında rastgele ondalıklı sayılar döner.


# 22 - vonmisesvariate(mu, kappa)               : Von Mises dağılımına göre rastgele bir ondalık sayı döndürür.

# 23 - weibullvariate(alpha, beta)              : Weibull dağılımına göre rastgele bir ondalık sayı döndürür.