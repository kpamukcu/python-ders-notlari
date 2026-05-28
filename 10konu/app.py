import streamlit as st

st.slider("Puan", 0, 100)

st.title('Merhaba Streamlit ile Title Yazdım')  ### H1 etiketli başlık
st.header('Bu bir başlık')                      ### H2 etiketli başlık
st.subheader('Bu bir alt başlık')               ### H3 etiketli başlık

st.write('Python ile web uygulamam')            ### p etiketli başlık 
st.text('Text ile yazılan yazı')                ### etiketsiz yazı
st.markdown('**Bu Kalın Yazıdır**')             ### Strong etiketi ile Kalın yazı yazmayı sağlar.

isim = st.text_input('Adınızı Girin', help='Adınızı ve Soyadınızı Girin', placeholder='Adınız')           ### Kullanıcıdan bilgi almak için kullanlır.
dogum = st.number_input('Doğum Yılınızı Girin', min_value=1900, max_value=2026)                           ### Kullanıcıdan sayısal bilgi almak için kullanlır.

if isim and dogum:
    if dogum<=2026:
        yas = 2026 - dogum
        if yas >= 18:
            st.write(f'Sayın {isim}, {yas} yaşındasınız. Ehliyet Başvurusu Yapabilirsiniz.')
        else:
            st.write(f'Sayın {isim}, {yas} yaşındasınız. {18-yas} yıl sonra başvuru yapabilirsiniz.')
    else:
        st.write('Doğum Yılınızı Doğru Girin')
else: ### Bu Blok Yazılmasa da Olur ###
    st.write('')


userName = st.text_input('Kullanıcı Adınızı Girin')
password = st.text_input('Şifrenizi Girin', type='password')

if userName == 'hayko' and password == '123':
    adres = st.text_input('Teslimat Adresini Girin')
    sehir = st.selectbox('Şehir', ['Ankara','Bursa','İstanbul','İzmir'], index=None, placeholder='Şehir Seçiniz')
    cinsiyet = st.radio('Cinsiyet: ', ['Erkek','Kadın'])
    mesaj = st.text_area('Not Ekleyin')
    onay = st.checkbox('Kvkk Metnini Onaylıyorum')
    

    if st.button('Sipariş Ver'):
        st.write(f'Sayın {userName} siparişiniz oanyalanmıştır.')
        st.write('Bilgileriniz:')
        st.write(f'Adres: {adres} / {sehir}')
        st.write(f'Mesajınız: {mesaj}')
        st.write(f'Cinsiyet: {cinsiyet}')
        if onay:
            st.write('Çerezlere Onay Verdiniz')
        else:
            st.write('Çerezlere Onay Vermediniz.')

soru = st.sidebar.chat_input('Soru Sor')

if soru:
    st.sidebar.chat_message('user').write(soru)
    st.sidebar.chat_message("assistant").write("Bunu aldım 👍")

# st.sidebar.title('Menü')
# st.sidebar.selectbox('Sayfalar',['Ana Sayfa','Blog','İletişim'])

st.success('Kayıt Başarılı')

kGiyim, eGiyim, cGiyim = st.tabs(['Kadın Giyim','Erkek Giyim','Çocuk Giyim'])

with kGiyim:
    st.write('En Kaliteli Kadın Giyim Ürünleri Bizde')

eGiyim.write('En Kaliteli Erkek Giyim Ürünleri Bizde')

cGiyim.write('En Kaliteli Çocuk Giyim ürünleri Bizde')

kadi = ''
sifre = ''

signin,login = st.tabs(['Üye Ol','Giriş Yap'])

with signin:
    st.title('Üye Olun')
    st.text_input('',placeholder='Adınız Soyadınız', label_visibility='collapsed')
    st.text_input('',placeholder='E-Posta Adresiniz', label_visibility='collapsed')