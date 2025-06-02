# Instagram Bote

Bu proje, kullanıcıların Instagram hesaplarındaki takipçi ve takip ettikleri kişileri analiz etmelerine yardımcı olan bir otomasyon aracıdır. Kullanıcılar kendi hesaplarına giriş yaptıktan sonra takipçi listeleri alınır ve analiz edilerek kullanıcıya takip etmeyenleri veya karşılıklı takipleşmediklerini gösterir.

## Özellikler

- **Giriş Sistemi**: Kullanıcı adı ve şifre ile Instagram'a giriş yapılabilir.
- **Takipçi ve Takip Edilenlerin Alınması**: Otomatik olarak tüm liste çekilir.
- **Kullanıcı Arayüzü (GUI)**: PyQt5 kullanılarak kullanıcı dostu bir arayüz sağlanmıştır.
- **Farklılık Analizi**: Takip etmeyenleri veya geri takip yapmayanları analiz ederek gösterir.
- **Excel Desteği**: Sonuçlar `.xlsx` dosyası olarak dışa aktarılır.
- **Dark Mode**: Karanlık tema desteği mevcuttur.

## Ekran Görüntüsü

> Uygulamanın arayüzünü çalıştırmak için `login.py` dosyasını çalıştırın.

## Kullanım

1. Gerekli kütüphanelerin yüklü olduğundan emin olun (aşağıda belirtildi).
2. `login.py` dosyasını çalıştırarak uygulamayı başlatın.
3. Kullanıcı adı ve şifrenizi girerek oturum açın.
4. Takipçi ve takip edilen listelerini çekin.
5. Farklılıkları analiz ederek sonuçları görüntüleyin veya dışa aktarın.

## Gereksinimler

Python 3.7+ sürümü önerilir.

Gerekli kütüphaneleri yüklemek için:

```bash
pip install -r requirements.txt
```

Veya ayrı ayrı:

```bash
pip install PyQt5 openpyxl selenium
```

Ayrıca, tarayıcı sürümünüze uygun bir **WebDriver** (ör. Chrome için chromedriver) indirip `webdriver.exe` olarak projenin içine eklemelisiniz.

## Dosya Yapısı

- `login.py`: Uygulamanın başlangıç dosyası.
- `compare_result.py`: Sonuçları karşılaştırır
- `insta.py`: Selenium ile Instagram işlemlerini otomatikleştiren bot mantığı.

## Kurulum

```bash
git clone https://github.com/ozay-mehmet/Instagram-Bote.git
cd App_Code
python login.py
```

## Uyarı

- Bu araç, Instagram’ın kullanım politikalarına aykırı işlemler yapabilir. Kendi hesabınızla dikkatli kullanın.
- Hesabınızın güvenliği için 2FA (iki faktörlü kimlik doğrulama) aktifse giriş sorunları yaşayabilirsiniz.

## Katkıda Bulunma

Pull request'ler her zaman memnuniyetle karşılanır. Büyük değişiklikler yapmadan önce bir issue açarak önerilerinizi tartışabilirsiniz.
