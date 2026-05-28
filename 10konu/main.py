""" 
Streamlit, Python ile çok hızlı şekilde web tabanlı arayüzler oluşturmayı sağlayan bir framework’tür.

Özellikle:
Veri analizi, Yapay zeka projeleri, Dashboard, Veri görselleştirme, Makine öğrenmesi demo uygulamaları için çok popülerdir.

Kurulumu:
pip install streamlit (Windows)
pip3 install streamlit (Mac)

Streamlit ile oluşturulan bir web uygulamasını çalıştırabilmek için  terminalde cd ile proje içine girilmeli ve streamlit run app.py yazılarak uygulama çalıştırılmalıdır.


Pip kurulumu yapıldıktan sonra proje içine Streamlit "import streamlit as st" şeklinde import edilir.

st.title('Ana Başlık')                  -> Büyük Başlık yazmayı sağlar.
st.header('Başlık')                     -> Başlık yazmayı sağlar.
st.subheader('Alt Başlık')              -> Alt Başlık yazmayı sağlar.
st.write('Düz Yazı')                    -> p etiketli düz metin yazar 
st.text('Düz Yazı')                     -> etiketsiz yazı
st.markdown('**Kalın Düz Yazı**')       -> Strong etiketi ile Kalın yazı yazmayı sağlar.


st.text_input('Label')                  -> Kullanıcıdan Bilgi Almak için kullanılır.

| Parametre          | Açıklama                       |
| ------------------ | ------------------------------ |
| `label`            | Input başlığı                  |
| `value`            | Varsayılan değer               |
| `max_chars`        | Maksimum karakter              |
| `placeholder`      | Gri açıklama yazısı            |
| `type`             | `"default"` veya `"password"`  |
| `help`             | Tooltip açıklaması             |
| `disabled`         | Input’u pasif yapar            |
| `label_visibility` | Label görünürlüğü              |
| `key`              | Benzersiz anahtar              |
| `autocomplete`     | Otomatik tamamlama             |
| `on_change`        | Değişince fonksiyon çalıştırır |
| `args`             | Fonksiyon argümanları          |



st.number_input('Label')                -> Kullanıcıdan Sayısal Bilgi Almak içib Kullanılır.
                                           min_value=1900, max_value=2026 parametreleri ile tanımlanabilir.


| Parametre          | Açıklama           |
| ------------------ | ------------------ |
| `label`            | Input başlığı      |
| `min_value`        | Minimum değer      |
| `max_value`        | Maksimum değer     |
| `value`            | Varsayılan değer   |
| `step`             | Artış miktarı      |
| `format`           | Görünüm formatı    |
| `placeholder`      | Input içi açıklama |
| `disabled`         | Pasif yapar        |
| `label_visibility` | Label görünürlüğü  |
| `key`              | Benzersiz anahtar  |
| `help`             | Tooltip açıklaması |


st.text_area('Label')                    -> Geniş Metin alanı için kullanılır.

| Parametre          | Açıklama                        |
| ------------------ | ------------------------------- |
| `label`            | Alan başlığı                    |
| `value`            | Varsayılan metin                |
| `height`           | Alan yüksekliği (px)            |
| `max_chars`        | Maksimum karakter               |
| `placeholder`      | Gri açıklama yazısı             |
| `help`             | Bilgi tooltip’i                 |
| `disabled`         | Alanı pasif yapar               |
| `label_visibility` | Label görünürlüğü               |
| `key`              | Benzersiz ID                    |
| `on_change`        | Değişince fonksiyon çalıştırır  |
| `args`             | on_change fonksiyon argümanları |


st.checkbox('Label')                                        -> Kullanıcıdan oany almak için kullanılır.
st.selectbox('label',['Option 1','Option 2','Option 3'],index=None, placeholder='Seçiniz')    -> Kullanıcıdan seçim alınır
st.button('Tıkla')      -> Form butonu oluşturur.
st.radio('Label',['Option 1','Option 2'])   -> Kullanıcıdan tek bir seçim yapması istenir.


 """