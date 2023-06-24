# modül nedir ? çok kullanılan fonksiyonların bir araya geldiği paketlere modül denir.

# math modulu 

# Python programlama dilinin standart kütüphanesinde bulunan bir matematiksel işlevler koleksiyonudur.
# Bu modül, matematikle ilgili çeşitli hesaplamaları yapabilmek için bir dizi işlev ve sabit sağlar



import math                               

# bu import yönteminde module ait değişken , metot , fonksiyon vs kullanılacaksa başına mutlaka "math." getirmek gerekir.

print(math.sqrt(64))   # / 8 
# print(pi)               # / NameError: name 'pi' is not defined
print(math.pi)          # / 3.141592653589793


from math import factorial , sqrt    

# bu import yönteminde module ait belli başlı ( factoriel , sqrt) fonksiyonlar çağırıldığından sadece bu fonksiyonlar kullanılır. "math." kullanmaya gerek yoktur.

print(factorial(5))     # / 120 
print(sqrt(9))          # / 3   


from math import *

# # bu import yönteminde module ait değişken , metot , fonksiyon vs kullanılacaksa başına mutlaka "math." getirmek gerekmez.


print(pow(2,3))     # / 8
print(pi)           # / 3.141592653589793


# math modulu içerisinde tanımlı fonksiyonlar.


# trigonometrik fonksiyonlar:

#  - math.acos(x)                                         : Verilen bir sayının ters kosinüsünü döndürür.
#  - math.acosh(x)                                        : Verilen bir sayının hiperbolik arkkosinüsünü döndürür.
#  - math.asin(x)                                         : Verilen bir sayının ters sinüsünü döndürür.
#  - math.asinh(x)                                        : Verilen bir sayının hiperbolik arksinüsünü döndürür.
#  - math.atan(x)                                         : Verilen bir sayının ters tanjantını döndürür.
#  - math.atan2(y, x)                                     : İki sayı arasındaki ters tanjantı döndürür. Y ve X koordinatlarını belirtir.
#  - math.atanh(x)                                        : Verilen bir sayının hiperbolik artanjantını döndürür.
#  - math.cos(x)                                          : Verilen bir sayının kosinüsünü döndürür.
#  - math.cosh(x)                                         : Verilen bir sayının hiperbolik kosinüsünü döndürür.
#  - math.sin(x)                                          : Verilen bir sayının sinüsünü döndürür.
#  - math.sinh(x)                                         : Verilen bir sayının hiperbolik sinüsünü döndürür.
#  - math.tan(x)                                          : Verilen bir sayının tanjantını döndürür.
#  - math.tanh(x)                                         : Verilen bir sayının hiperbolik tanjantını döndürür.
#  - math.degrees(x)                                      : Verilen bir açıyı derece cinsinden döndürür.
#  - math.radians(x)                                      : Verilen bir açıyı radyan cinsinden döndürür.
#  - math.hypot(x, y)                                     : İki dik kenarın uzunluğunu vererek hipotenüs uzunluğunu döndürür.

# logaritmik fonksiyonlar:

#  - math.exp(x)                                          : Verilen bir sayının e üzeri x (e^x) değerini döndürür.
#  - math.expm1(x)                                        : Verilen bir sayının e üzeri x - 1 (e^x - 1) değerini döndürür.
#  - math.log(x, base)                                    : Verilen bir sayının belirli bir tabanda logaritmasını döndürür.
#  - math.log10(x)                                        : Verilen bir sayının 10 tabanındaki logaritmasını döndürür.
#  - math.log1p(x)                                        : Verilen bir sayının 1 artı x değerinin logaritmasını döndürür.
#  - math.log2(x)                                         : Verilen bir sayının 2 tabanındaki logaritmasını döndürür.
#  - math.lgamma(x)                                       : Verilen bir sayının log-gamma fonksiyonunu döndürür.


# aritmatik fonksiyonlar

#  - math.copysign(x, y)                                  : Y değerinin işaretini X değerine kopyalar ve sonucu döndürür.
#  - math.fabs(x)                                         : Verilen bir sayının mutlak değerini döndürür.
print(math.fabs(-5))        # / 5
#  - math.factorial(x)                                    : Verilen bir sayının faktöriyelini döndürür.
print(math.factorial(5))    # / 120
#  - math.fmod(x, y)                                      : X sayısının Y sayısına bölümünden kalanı döndürür.
print(math.fmod(8,3))       # / 2
#  - math.frexp(x)                                        : Verilen bir sayının katsayı ve üs bileşenlerini döndürür. ( mantissa sayısı , üstel sayı)
print(math.frexp(9))        # / (0.5625, 4)
#  - math.gamma(x)                                        : Verilen bir sayının gamma fonksiyonunu döndürür.
#  - math.isclose(a, b, *, rel_tol=1e-09, abs_tol=0.0)    : İki sayının yakınlığını kontrol eder.
#  - math.isfinite(x)                                     : Verilen bir sayının sonlu (finite) olup olmadığını kontrol eder.
#  - math.isinf(x)                                        : Verilen bir sayının sonsuz (∞) olup olmadığını kontrol eder.
#  - math.isnan(x)                                        : Verilen bir sayının NaN (Not a Number) olup olmadığını kontrol eder.
#  - math.ldexp(x, i)                                     : X sayısını 2^i ile çarparak sonucu döndürür.
#  - math.nextafter(x, y)                                 : X sayısının Y sayısından sonraki takip eden kayan nokta sayısını döndürür.
#  - math.pow(x, y)                                       : X sayısının Y üssünü döndürür.
print(math.pow(2,3))        # / 8


# hata fonksiyonları

#  - math.erf(x)                                          : Verilen bir sayının hata fonksiyonunu döndürür.
#  - math.erfc(x)                                         : Verilen bir sayının tamamlanmış hata fonksiyonunu döndürür.


# obeb fonksiyonları :

#  - math.gcd(a, b)                                       : Verilen iki sayının en büyük ortak bölenini döndürür.
print(math.gcd(3,6))        # / 3


# karekök fonksiyonları :

#  - math.sqrt(x)                                         : Verilen bir sayının karekökünü döndürür.
print(math.sqrt(25))        # / 5


# iterasyon fonksiyonları:

#  - math.fsum(iterable)                                  : İterasyon yapılabilecek bir dizi veya iterable üzerinde hassas kayan nokta toplamını döndürür.
#  - math.prod(iterable, *, start=1)                      : İterasyon yapılabilecek bir dizi veya iterable üzerinde elemanların çarpımını döndürür.


# Yuvarlama fonksiyonları:

#  - math.ceil(x)                                         : Verilen bir sayının en küçük tam sayıya yukarı yuvarlanmış halini döndürür.
print(math.ceil(3.1))   # / 4
#  - math.floor(x)                                        : Verilen bir sayının en büyük tam sayıya aşağı yuvarlanmış halini döndürür.
print(math.floor(3.9))  # / 3
#  - math.modf(x)                                         : Verilen bir sayının ondalık kısmını ve tamsayı kısmını ayrı ayrı döndürür.
print(math.modf(3.25))  # / (0.25, 3.0)
#  - math.trunc(x)                                        : Verilen bir sayının tamsayı kısmını döndürür.
print(math.trunc(8.9))  # / 8

