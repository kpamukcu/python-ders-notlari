""" 
VERİ GÖRSELLEŞTİRME (Data Visualization)
Ham verilerin grafikler, tablolar, diyagramlar ve çeşitli görsel araçlar kullanılarak daha anlaşılır, yorumlanabilir ve analiz edilebilir hale getirilmesidir.
Başka bir ifadeyle, sayısal veya kategorik verileri görsel bir forma dönüştürerek verilerin taşıdığı anlamı daha kolay ortaya çıkarmaktır.

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


-   plt.show()      -> Oluşturulan grafiği ekrana getirir.
-   plt.title()     -> Grafiğin Başlığını Belirler
-   plt.xlabel()    -> X Ekseninin adını belirler
-   plt.ylabel()    -> y ekseninin adını belirler
-   plt.plot(x Ekseni, y Ekseni)    -> Çizgi grafik oluşturur.
-   plt.scatter(x Ekseni, y Ekseni)  -> Nokta Grafik oluşturur.
-   plt.bar(x ekseni, y ekseni)     -> Dikey Bar Grafiği Oluşturur
-   plt.barh(x ekseni, y ekseni)    -> Yatay Bar Grafiği Oluşturur

Veri görselleştirme nedir? Ne işe Yarar? Hangi Durumlar için veri görselleştirme ihtiyacı duyulur?
"""


""" 
Plot Grafiği (Çizgi Grafik)
Plot grafiği, iki veya daha fazla veri noktası arasındaki değişimi çizgilerle gösteren grafik türüdür.

En çok şu durumlarda kullanılır:
- Günlük, haftalık veya aylık satış değişimleri
- Web sitesi ziyaretçi sayısının zaman içindeki değişimi
- Google Ads kampanyalarının performansı
- Aylık gelir ve gider takibi
- Bir ürünün fiyat değişimi
- Spor performansının gelişimi

"""

import matplotlib.pyplot as plt

aylar = ['Ocak','Şubat','Mart','Nisan','Mayıs']
satislar = [120,180,150,250,300]

plt.plot(aylar,satislar)    ## color='blue' ile renk, linewidth=2 ile çizgi kalınlığı, linestyle="--" çizgi türü, marker='0' ile kesişim noktlarının şekli ile özelleştirilebilir. 
plt.show()

### Mini Örnek 1 ###
### Haftaya ait her günün web sitesi ziyaretçi adetlerini grafikleştirin

gunler = ['Pazartesi','Salı','Çarşamba','Perşembe','Cuma']
ziyaretci = [450,520,480,700,850]

plt.plot(gunler,ziyaretci)
plt.show()

### Not: gunler ve ziyaretci listelerindeki eleman sayılarının eşit olması gerekiyor. Çünkü her günün karşısında bir ziyaretçi değeri bulunuyor.


### Mini Örnek 2 ###
### 1) Günlük reklam harcamasını gösteren grafik.
### 2) Günlük dönüşüm sayısını gösteren grafik.
gun = ['Pzt','Salı','Çrş','Prş','Cuma','Cmt','Paz']
reklam_harcamasi = [500,650,600,800,950,700,1100]
donusum = [12,15,14,20,24,18,30]


plt.xlabel('Günler')
plt.ylabel('Reklam Harcaması')
plt.title('Günlük Reklama Harcaması Grafiği')
plt.plot(gun,reklam_harcamasi,color="#00ffff",marker="o")
plt.show()


plt.title('Günlük Dönüşüm Sayısı Grafiği')
plt.xlabel('Günler')
plt.ylabel('Dönüşüm Adeti')
plt.plot(gun,donusum,color="red",marker="o")
plt.show()

## Not: iki grafik aynı grafik alanında görünür. Eğer ayrı ayrı göstermek istersen plt.figure() fonksiyonu ile yeni bir grafik alanı oluşturabiliriz. 



""" 
Scatter Grafiği (Dağılım Grafiği)

Scatter grafiği, veri analizinde oldukça önemli bir yere sahiptir. Özellikle veri setlerinde değişkenler arasındaki ilişkileri keşfetmek, kümelenmeleri görmek ve sıra dışı değerleri tespit etmek için kullanılır.

Scatter Plot (Dağılım Grafiği), iki sayısal değişkenin birbirleriyle olan ilişkisini koordinat düzleminde noktalar kullanarak gösteren grafik türüdür.

Her nokta, veri setindeki bir gözlemi temsil eder.

Örneğin bir spor salonundaki kişilerin haftalık antrenman süreleri ile yaktıkları kaloriler arasındaki ilişkiyi incelemek istiyoruz.

Kişi	Antrenman süresi (saat)	        Yakılan kalori
A	            1	                        200
B	            2	                        350
C	            3	                        500
D	            4	                        650
E	            5	                        800

Burada:
- X ekseni: Antrenman süresi
- Y ekseni: Yakılan kalori
- Her nokta: Bir kişiyi temsil eder.

Scatter grafiği hangi durumlarda kullanılır?
Örneğin:
X değişkeni	                Y değişkeni	            İncelenen ilişki
Reklam bütçesi	            Satış miktarı	        Bütçe satışları etkiliyor mu?
Web sitesi ziyaretçisi	    Form sayısı	            Trafik dönüşümle ilişkili mi?
Ürün fiyatı	                Satış adedi	            Fiyat arttıkça satış azalıyor mu?
Antrenman süresi	        Yakılan kalori	        Süre ve kalori ilişkili mi?
Yaş	                        Harcama miktarı	        Yaş ve harcama arasında ilişki var mı?


Değişkenler arasındaki ilişkiyi yorumlamak
Scatter grafiğinde üç temel ilişki biçimiyle karşılaşabiliriz. 
1. Pozitif ilişki (Positive Correlation): Bir değişken artarken diğer değişken de genel olarak artar. Örnek: Reklam bütçesi yükseldikçe satış miktarının artması.
2. Negatif ilişki (Negative Correlation): Bir değişken artarken diğer değişken genel olarak azalır. Örnek: Ürün fiyatı yükseldikçe satış miktarının azalması.
3. İlişkisiz veya zayıf ilişki (No or Weak Correlation): İki değişken arasında belirgin bir doğrusal ilişki görülmez.

Önemli: Scatter grafiğinde bir ilişki görülmesi, bir değişkenin diğerine kesin olarak neden olduğunu kanıtlamaz. Korelasyon ile nedensellik farklı kavramlardır.
"""

antrenman = [1,2,3,4,5]             ## Saat olarak antrenamn süresi
kalori = [200,350,500,650,800]      ## Harcanan Kalori

plt.scatter(antrenman,kalori)       ##Örneğin color='red' ile renk, s=100 ile boyut, marker='o' ile grafiği özelleştirebiliriz.
plt.show()

### Önemli Not: İki listedeki aynı indeks numarasına sahip değerler birbiriyle eşleştirilir.

#### Mini Uygulama - Reklam Bütçesi ve Satış Adeti Korelasyonu ####

reklam_butcesi = [1000,1500,2000,2500,3000,3500]
satis_adeti = [12,18,20,28,32,40]

plt.scatter(reklam_butcesi,satis_adeti,color="#007bff",s=80)
plt.show()


""" 
Bar Chart (Sütun Grafik)

Bar grafiği, farklı kategorilerin değerlerini karşılaştırmak için kullanılır.
Bar grafiği, kategorilere ait sayısal değerleri sütunlar aracılığıyla karşılaştırmayı sağlar.
Özellikle dijital pazarlama, satış raporlaması, müşteri analizi ve performans ölçümünde oldukça kullanışlıdır.

Örneğin:
- Hangi ayda daha fazla satış yapılmış?
- Hangi reklam kampanyası daha fazla dönüşüm sağlamış?
- Hangi ürün daha fazla satılmış?
- Hangi web sitesi kanalı daha fazla ziyaretçi getirmiş?
"""

aylar = ['Ocak','Şubat','Mart','Nisan','Mayıs']
satislar = [120,180,150,250,300]

plt.bar(aylar,satislar, edgecolor="black")     ## Özelleştirme için color, width(kalınlık ör:0.6), edgecolor(sütunların kenarlık rengi) parametreleri kullanılabilir.
plt.show()


urunler = ['Bilgisayar','Telefon','Tablet','Kulaklık']
satislar = [45,120,65,90]


plt.barh(urunler,satislar, color="Green")
plt.title('Ürün Satış Performansı')
plt.xlabel('Satışlar')
plt.ylabel('Ürünler')
plt.show()

### Mini Uygulama - Dijital Pazarlama Kampanya Karşılaştırması
### Sütun rengini belirle
### Grafiğe başlık ekle
### X ve Y eksenlerine isim ver
### Yatay bar sütun olsun

kanallar = ['Google Ads','Meta Ads','Organik SEO','E-Posta']
donusumler = [120,95,160,75]

plt.title('Kanal Performans Karşılaştırması')
plt.xlabel('Dönüşümler')
plt.ylabel('Kanallar')
plt.barh(kanallar,donusumler, color="red", height=0.5)
plt.show()