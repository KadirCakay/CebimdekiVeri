


# 💰 CebimdekiVeri (PocketData)
### Kişisel Bütçe Takibi ve Yapay Zeka Destekli Gelecek Tahmini

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![AI](https://img.shields.io/badge/AI-Scikit%20Learn-orange?style=for-the-badge)
![Data](https://img.shields.io/badge/Data-Pandas%20%7C%20Matplotlib-green?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-lightgrey?style=for-the-badge)

**CebimdekiVeri**, kullanıcıların gelir ve giderlerini takip etmesini sağlayan, geçmiş verileri analiz ederek **Makine Öğrenmesi (Machine Learning)** algoritmalarıyla gelecek ayki finansal durumlarını tahmin eden akıllı bir terminal uygulamasıdır.

Bu proje, **Sistem Analizi ve Tasarımı** dersi kapsamında; modern yazılım mühendisliği prensipleri ve **Tasarım Desenleri (Design Patterns)** kullanılarak geliştirilmiştir.

---

## 🚀 Öne Çıkan Özellikler

* **📊 Kişiselleştirilmiş Veri Simülasyonu:** Program ilk açıldığında, kullanıcının gerçek hayat parametrelerine (Kira, Market, Maaş vb.) göre **2 yıllık** gerçekçi bir geçmiş veri seti oluşturur.
* **🤖 Yapay Zeka (Linear Regression):** Geçmiş harcama trendlerini ve eğimini analiz ederek, gelecek ayın tahmini gelir/giderini %90+ tutarlılıkla hesaplar.
* **🔔 Akıllı Bildirim Sistemi (Observer Pattern):** Bakiye kritik seviyeye düştüğünde sistem kullanıcıyı otomatik olarak uyarır (Event-Driven).
* **📈 Görsel Analiz:** Harcama dağılımını **Pasta Grafiği**, finansal trendi ve AI tahminini **Çizgi Grafiği** ile görselleştirir.
* **💾 Kalıcı Veri (CSV):** Tüm işlemler `csv` formatında saklanır, program kapatılıp açılsa bile veri kaybı yaşanmaz.

---

## 🏗️ Yazılım Mimarisi ve Tasarım Desenleri

Proje, **"Separation of Concerns"** (İlgi Alanlarının Ayrılması) prensibine göre modülerize edilmiştir. Aşağıdaki tasarım desenleri aktif olarak kullanılmıştır:

| Desen (Pattern) | Kullanım Amacı | Uygulandığı Sınıf |
| :--- | :--- | :--- |
| **Singleton** | Tüm sistemde tek bir yönetici olması ve veri tutarlılığı. | `ButceYonetici` |
| **Observer** | Bakiye değiştiğinde kullanıcının otomatik uyarılması. | `Kullanici` (Listener) |
| **Factory** | Rapor oluşturma sürecinin soyutlanması. | `RaporFactory` |
| **Template Method** | İşlem (Gelir/Gider) sınıflarının ortak bir atadan türetilmesi. | `Islem` (Abstract) |

---

## 🛠️ Kurulum ve Çalıştırma

Projeyi bilgisayarınızda çalıştırmak için aşağıdaki adımları izleyin:

### 1. Repoyu Klonlayın
```bash
git clone [https://github.com/KULLANICI_ADIN/CebimdekiVeri.git](https://github.com/KULLANICI_ADIN/CebimdekiVeri.git)
cd CebimdekiVeri
````

### 2\. Gerekli Kütüphaneleri Yükleyin

```bash
pip install -r requirements.txt
```

### 3\. Veri Setini Oluşturun (Opsiyonel)

Eğer ilk kez çalıştırıyorsanız, test verisi üretmek için:

```bash
python veri_uretici.py
```

### 4\. Uygulamayı Başlatın

```bash
python main.py
```

-----

## 📂 Proje Yapısı

```text
CebimdekiVeri/
│
├── main.py              # Uygulamanın giriş noktası (Arayüz)
├── sistem_modelleri.py  # Design Patterns, Class Yapıları ve Veri Yönetimi
├── analiz_motoru.py     # Scikit-Learn ile AI Hesaplamaları (Logic)
├── grafik_cizici.py     # Matplotlib ile Görselleştirme (View)
├── veri_uretici.py      # Sentetik Veri Simülasyon Aracı
├── butce_verisi.csv     # Veritabanı (Otomatik oluşur)
└── requirements.txt     # Kütüphane bağımlılıkları

    `![Grafik Analizi](sunum_grafikleri.png)`
    yazman yeterli.
```
