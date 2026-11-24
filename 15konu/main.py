""" 
VERİ GÖRSELLEŞTİRME

1. Matplotlib Kütüphanesi
    Matplotlib, Python'da verileri grafiklere dönüştürmek için kullanılan bir veri görselleştirme kütüphanesidir.
    Örneğin elimizde ay bazlı olarak yapılan satış adetleri tablosu var. Bu tabloyu grafik üzerinde gösterebiliriz.
    Matplotlib ile çizgi, sütun, pasta, dağılım ve daha birçok grafik oluşturabilir.
    
    pip install matplotlib              ile terminal üzerinden kurulumu yapılmaldır.
    import matplotlib.pyplot as plt     ile kütüphane projeye dahil edilir.

    Kod	            Açıklama
    matplotlib	    Ana kütüphane
    pyplot	        Grafik oluşturma araçlarını içeren modül
    plt	            pyplot için kullandığımız kısa isim (alias)


-   plt.show()    -> Oluşturulan grafiği ekrana getirir.
-   plt.plot(x Ekseni, y Ekseni)   -> Çizgi grafik oluşturur.

Veri görselleştirme nedir? Ne işe Yarar? Hangi Durumlar için veri görselleştirme ihtiyacı duyulur?
"""

import matplotlib.pyplot as plt

aylar = ['Ocak','Şubat','Mart','Nisan','Mayıs']
satislar = [120,180,150,250,300]

plt.plot(aylar,satislar)
plt.show()

### Mini Örnek ###
### Haftaya ait her günün web sitesi ziyaretçi adetlerini grafikleştirin

gunler = ['Pazartesi','Salı','Çarşamba','Perşembe','Cuma']
ziyaretci = [450,520,480,700,850]

plt.plot(gunler,ziyaretci)
plt.show()

### Not: gunler ve ziyaretci listelerindeki eleman sayılarının eşit olması gerekiyor. Çünkü her günün karşısında bir ziyaretçi değeri bulunuyor.