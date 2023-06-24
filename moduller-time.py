import time

# # tanımı : zaman ile ilgili fonksiyonları içinde barındıran modüldür.
# # sonuc=print(time.time())        # / 1 ocak 1970 den günümüze geçen zamanın saniye cinsinden değeri. 1681161631.4000869


# baslangic = time.time()
# liste=[]
# for i in range(100000):
#     liste.append(i)
# bitis = time.time()

# gecen_zaman=bitis-baslangic
# print(gecen_zaman)              # / 1000000 tane i içeren bir listeyi kaç saniyede oluşturğunu sorguladık.

# yukardaki fonksiyonu 2 algoritma arasında hangisinin daha hızlı çalıştığını test etmek için kullanabiliriz.

# ctime fonksiyonu : 

print(time.ctime())                                 # / Parantez içinde herhangi bir değer yoksa güncel zamanı verir. Tue Apr 11 00:49:16 2023 , str döner
print(time.ctime(100000))                           # / parantez içinde bir ifade varsa 1 ocak 1970 tarihinin üstüne o kadar saniye ekler. Fri Jan  2 06:46:40 1970 , str döner
print(time.localtime())                             # / time.struct_time(tm_year=2023, tm_mon=4, tm_mday=11, tm_hour=0, tm_min=54, tm_sec=31, tm_wday=1, tm_yday=101, tm_isdst=0)
print(time.localtime(1000000))                      # / ctime ile aynı davranır. 1 ocak 1970 e saniye olarak ekler ve localtime olarak döner.
print(time.asctime())                               # / herhangi bir değer vermez isek ctime gibi çalışır. ana görevi localtime ı okunabilir hale getirmek.
print(time.strftime("%d:%h:%Y %H:%M:%S %p"))        # / istediğimiz şekilde çıktı ayarlayabildiğimiz bir fonksiyondur. 11:Apr:2023 01:09:50 AM
print(time.sleep(5))                                # / 5 saniye es vermeye yarar.

# 1  - time.time() fonksiyonu            : 
# 2  - time.asctime() fonksiyonu         : 
# 3  - time.ctime() fonksiyonu           :      
# 4  - time.get_clock_info() fonksiyonu  : 
# 5  - time.gmtime() fonksiyonu          :
# 6  - time.localtime() fonksiyonu       : 
# 7  - time.mktime() fonksiyonu          :
# 8  - time.monotonic() fonksiyonu       :
# 9  - time.monotonic_ns() fonksiyonu    :
# 10 - time.perf_counter() fonksiyonu    :
# 11 - time.perf_counter_ns() fonksiyonu :
# 12 - time.process_time() fonksiyonu    :
# 13 - time.process_time_ns() fonksiyonu :
# 14 - time.sleep() fonksiyonu           :
# 15 - time.strftime() fonksiyonu        :
# 16 - time.strptime() fonksiyonu        :
# 17 - time.thread_time() fonksiyonu     :
# 18 - time.thread_time_ns() fonksiyonu  :
# 19 - time.time_ns() fonksiyonu         :