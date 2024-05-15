# import matematik  -> matematik modülünün tamamı program olarak eklendi. İçindeki fonksiyonlara bu dosyada tek tek ulaşamayız
# from matematik import *   -> matemetik modülünün tamamı program olarak yüklendi ve içindeki tüm fonksiyonlara tektek ulaşabiliriz
# from matematik import carp   -> matematik modülünün tamamı program olarak yüklendi ve içindeki carp() fonksiyonuna tek başına da ulaşabiliriz. Diğer fonksiyon veya fonksiyonlar çağırıldığında tek başlarına çalışmayacaklardır.

from matematik import carp #Matematik modülündeki tüm fonksiyonlar program olarak çalışacak ve carp() fonksiyonuna bu dosya içinde tek başına da ulaşılabilir.

carp(4,3)


### Modül import etme yöntemleri ###

import math # math modülünün tamamını yükeldi
print(math.sqrt(9)) #sqrt -> karekök alma fonksiyonudur.

### Eğer birden fazla modül eklenecekse tek tek yazmak yerine import math , random şeklinde de eklenebilir.
### import math ile modülün tamamı yükleniyor bu durumda da hafızada fazla yer kaplayacaktır. O modül içindeki tek bir fonksiyon da çağırılabilir. "from math import çağırılacakfonksiyonAdı" ile yapılabilir.

# from math import sqrt ile import yapıldıktan sonra
# print(math.sqrt(9)) yerine print(sqrt(9)) kullanılabilir.
# Böylelikle 

from math import sqrt
print(sqrt(100))

# from math import * ile tüm fonksiyoları modül içinde yüklenmiş oluyor.
# Bu şekilde kullanımda da aynı şekilde sadece fonksiyon adı kullanılarak çalıştırılabilir. Ör: print(sqrt(100))

# Eğer import edileek modülün adı uzunsa kıslatmak için "import modulunUzunAdi as kısaAd" şeklinde tüm modül çağırılabilir.
# Ör: import math as m şeklinde yüklenen modülü print(m.sqrt(100)) şeklinde çalıştırmış oluruz.
