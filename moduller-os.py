# import os

# tanımı : bu modul işletim sistemi ile ilgili fonksiyonları barındırır. 
# bu modul yardımı ile dosyalar arasında gezinebiliriz.
# kalsorlerin içeriğini görüntüleyebiliriz.
# dosyalara yeni isimler verebiliriz.
# dosyaları klasörleyebiliriz.

# print(os.getcwd())                                          # / C:\Users\sahin\Desktop\Moduller
# os.chdir("/Users/sahin/Desktop/Moduller/deneme-modulu")     # / ayıraca dikkat.
# print(os.getcwd())                                          # / C:\Users\sahin\Desktop\Moduller\deneme-modulu
# print(os.listdir())                                         # / ['deneme1', 'deneme1 - Kopya', 'deneme1 - Kopya (2)', 'deneme1 - Kopya (3)', 'deneme1 - Kopya - Kopya', 'deneme1 - Kopya - Kopya (2)']
# listdir fonksiyonu parantez içi boş ise içerisinde bulunduğumuz klasörün dosyalarını liste olarak bize gönderir. 
# eğer klasör boş ise boş bir liste gönderir.
# parantez içinde içerisinde bulunmadığımız dosyayı yazarsak o dosyanın klasörlerini getirir.
# listdir sonucunu yan yana değil de alt alta yazdırmak istersek for döngüsünden faydalanmak gerekir.

# for dosya in os.listdir():
#     print(dosya)

# print : 
# deneme1
# deneme1 - Kopya
# deneme1 - Kopya (2)
# deneme1 - Kopya (3)
# deneme1 - Kopya - Kopya
# deneme1 - Kopya - Kopya (2)

# os.mkdir("mkdir-dosyası")                  # / içinde bulunduğumuz klasöre "mkdir-dosyası" adında bir klasör ekledik.
# os.mkdir("mkdir dosyası 2")                # / içinde bulunduğumuz klasöre "mkdir dosyası 2" adında bir klasör ekledik.
# os.makedirs("danama1/danama2/danama3")     # / içinde bulunduğumuz klasöre iç içe klasör ekledik. slaş yönü önemli
# os.rmdir("mkdir-dosyası")                  # / "mkdir-dosyası" isimli klasör silindi.
# os.removedirs("danama1/danama2/danama3")     # / iç içe boş klasörleri sildi. boş değilse silmez. en içten sile sile gelir.


# os.chdir("/Users/sahin/Desktop/Moduller/deneme-modulu/danama1/danama2")     # / chdir ile yoldan dosya içerisine girdik (girmeden de silebilirdik)
# os.remove(os.listdir()[0])                                                  # / danama2 klasörü içindeki elemanları listeledik ve 0.indexi remove ettik.

# os.chdir("/Users/sahin/Desktop")

# print(os.listdir("/Users/sahin/Desktop/Moduller/deneme-modulu/danama1/danama2"))
# silinecek = os.listdir("/Users/sahin/Desktop/Moduller/deneme-modulu/danama1/danama2")[0]

# print(silinecek)

# os.remove("/Users/sahin/Desktop/Moduller/deneme-modulu/danama1/danama2/" + silinecek)

# os.remove("/Users/sahin/Desktop/Moduller/deneme-modulu/danama1")

# print(os.listdir("/Users/sahin/Desktop/Moduller/"))

# print(os.getcwd())

# os.rename("Yeni Microsoft Word Document.docx","yeni oluşturulan dosya.docx") // içinde bulunmadığımız dosyada bu işlemi yapmak için dosyanın tam yolunu girmemiz gerekirdi.

# print(os.listdir("/Users/sahin/Desktop/Moduller/"))

# for gecerli_klasor , icindeki_klasorler , icindeki_dosyalar in os.walk("/Users/sahin/Desktop/Moduller/"):
#     print("Gecerli Klasör : " , gecerli_klasor)
#     print("icindeki klasörler" , icindeki_klasorler)
#     print("İçindeki Dosyalar" , icindeki_dosyalar)
#     print("------------------------")

# os modulu fonksiyonları

# 1  - os.abort() fonksiyonu                  : 
# 2  - os.access() fonksiyonu                 : 
# 3  - os.add_dll_directory() fonksiyonu      : 
# 4  - os.chdir() fonksiyonu                  : Klasör değiştirme foksiyonu (işaretin yönü önemli) parantez içi boş kalmamalı.
# 5  - os.chmod() fonksiyonu                  : 
# 6  - os.close() fonksiyonu                  : 
# 7  - os.closerange() fonksiyonu             : 
# 8  - os.cpu_count() fonksiyonu              : 
# 9  - os.device_encoding() fonksiyonu        : 
# 10 - os.dup() fonksiyonu                    : 
# 11 - os.dup2() fonksiyonu                   : 
# 12 - os.execvpe() fonksiyonu                : 
# 13 - os.execl() fonksiyonu                  : 
# 14 - os.execle() fonksiyonu                 :
# 15 - os.execlp() fonksiyonu                 : 
# 16 - os.execlpe() fonksiyonu                : 
# 17 - os.execv() fonksiyonu                  : 
# 18 - os.execve() fonksiyonu                 :  
# 19 - os.execvp() fonksiyonu                 : 
# 20 - os.execvpe() fonksiyonu                : 
# 21 - os.fdopen() fonksiyonu                 : 
# 22 - os.fsdecode() fonksiyonu               : 
# 23 - os.fspath() fonksiyonu                 : 
# 24 - os.fstat() fonksiyonu                  : 
# 25 - os.fsync() fonksiyonu                  : 
# 26 - os.ftruncate() fonksiyonu              : 
# 27 - os.get_exec_path() fonksiyonu          : 
# 28 - os.getcwd() fonksiyonu                 : 
# 29 - os.get_exec_path() fonksiyonu          : 
# 30 - os.get_handle_inheritable() fonksiyonu : 
# 31 - os.get_inheritable() fonksiyonu        : 
# 32 - os.get_terminal_size() fonksiyonu      :    
# 33 - os.getcwd() fonksiyonu                 :  # içinde bulunduğumuz dosyanın konumunu verir.
# 34 - os.getcwdb() fonksiyonu                : 
# 35 - os.getenv() fonksiyonu                 : 
# 36 - os.getlogin() fonksiyonu               : 
# 37 - os.getpid() fonksiyonu                 : 
# 38 - os.getppid() fonksiyonu                : 
# 39 - os.isatty() fonksiyonu                 : 
# 40 - os.kill() fonksiyonu                   : 
# 41 - os.link() fonksiyonu                   : 
# 42 - os.listdir() fonksiyonu                : # içinde bulunduğumuz dosyadaki kalsörleri liste tipinde döner.
# 43 - os.lseek() fonksiyonu                  : 
# 44 - os.lstat() fonksiyonu                  : 
# 45 - os.makedirs() fonksiyonu               : # içerisinde bulunduğumuz klasöre iç içe klasörler ekleme fonksiyondur.
# 46 - os.mkdir() fonksiyonu                  : # içerisinde bulunduğumuz klasöre yeni bir klasör ekleme fonksiyonudur.
# 47 - os.open() fonksiyonu                   : 
# 48 - os.pipe() fonksiyonu                   : 
# 49 - os.popen() fonksiyonu                  : 
# 50 - os.putenv() fonksiyonu                 : 
# 51 - os.read() fonksiyonu                   : 
# 52 - os.readlink() fonksiyonu               : 
# 53 - os.remove() fonksiyonu                 : # içinde bulunduğumuz klasörden herhangi bir fonksiyon silen fonksiyondur.
# 54 - os.removedirs() fonksiyonu             : # iç içe klasörleri silen fonksiyondur. içerden sile sile gelir. dolu dosya görünce durur.
# 55 - os.rename() fonksiyonu                 : # dosya ismi değiştirmeye yarar. dosya konumunu da değiştirebiliriz. 
# 56 - os.replace() fonksiyonu                : 
# 57 - os.rmdir() fonksiyonu                  : # içerisinde bulunduğumuz klasörden tek bir dosya silme fonksiyonudur.
# 58 - os.renames() fonksiyonu                : 
# 59 - os.scandir() fonksiyonu                : 
# 60 - os.set_handle_inheritable() fonksiyonu : 
# 61 - os.set_inheritable() fonksiyonu        : 
# 62 - os.spawnl() fonksiyonu                 : 
# 63 - os.spawnle() fonksiyonu                : 
# 64 - os.spawnv() fonksiyonu                 : 
# 65 - os.spawnve() fonksiyonu                : 
# 66 - os.startfile() fonksiyonu              : 
# 67 - os.stat() fonksiyonu                   : dosya hakkında bilgiler verir. ne zaman oluşturuldu , boyutu ne kadar vs.
# 68 - os.symlink() fonksiyonu                : 
# 69 - os.system() fonksiyonu                 : 
# 70 - os.times() fonksiyonu                  : 
# 71 - os.truncate() fonksiyonu               : 
# 72 - os.umask() fonksiyonu                  : 
# 73 - os.unlink() fonksiyonu                 : 
# 74 - os.unsetenv() fonksiyonu               : 
# 75 - os.urandom() fonksiyonu                : 
# 76 - os.utime() fonksiyonu                  : 
# 77 - os.waitpid() fonksiyonu                : 
# 78 - os.waitstatus_to_exitcode() fonksiyonu : 
# 79 - os.walk() fonksiyonu                   : bütün klasörü içerisindekiler ile birlikte listelemeye yarar.
# 80 - os.write() fonksiyonu                  : 
# 81 - os.path.join() fonksiyonu              : dosya yolu yapmaya yarar.
# 82 - os.path.isfile() fonksiyonu            : parantez içindeki girilen yol bir dosya mı ? sonuç true ya da false olarak gelir.
# 83 - os.path.splitext() fonksiyonu          : dosyayı uzantısından bölerek 2 elemanlı bir liste verir.
