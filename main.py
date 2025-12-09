import sys
from sistem_modelleri import ButceYonetici, Kullanici, Gelir, Gider, RaporFactory
import grafik_cizici  # YENİ MODÜL ADI


def menuyu_goster():
    print("\n" + "=" * 45)
    print("   CEBİMDEKİ VERİ - PROFESYONEL SÜRÜM   ")
    print("=" * 45)
    print("1. ➕ Gelir Ekle")
    print("2. ➖ Gider Ekle")
    print("3. 💰 Güncel Bakiye (Otomatik Hesaplanır)")
    print("4. 📈 Yapay Zeka Analizi (Grafik)")
    print("5. 📄 Rapor Oluştur")
    print("6. ❌ Çıkış")
    print("=" * 45)


def tarih_sor():
    tarih = input("Tarih (YYYY-AA-GG) [Boş bırakırsan BUGÜN]: ")
    return tarih.strip() if tarih.strip() != "" else None


def uygulamayi_baslat():
    yonetici = ButceYonetici()

    print("\n👋 Merhaba! CebimdekiVeri v2.0 Başlatıldı.")
    ad = input("Adınız: ") or "Admin"
    soyad = input("Soyadınız: ") or "User"

    kullanici = Kullanici(ad, soyad)
    yonetici.gozlemci_ekle(kullanici)

    print(f"\nHoş geldin {ad}. Sistem açılışta geçmiş verileri taradı ve bakiyeni güncelledi.")
    yonetici.bakiye_goster()  # Açılışta doğru bakiyeyi göster

    while True:
        menuyu_goster()
        secim = input("👉 Seçiminiz (1-6): ")

        if secim == '1':
            try:
                tutar = float(input("Gelir Tutarı (TL): "))
                aciklama = input("Açıklama: ")
                kaynak = input("Kaynak: ")
                tarih_str = tarih_sor()

                yonetici.islem_ekle(Gelir(tutar, aciklama, kaynak, tarih_str))
            except ValueError:
                print("❌ Hata: Tutar sayı olmalı!")

        elif secim == '2':
            try:
                tutar = float(input("Gider Tutarı (TL): "))
                aciklama = input("Açıklama: ")
                kategori = input("Kategori: ")
                tarih_str = tarih_sor()

                yonetici.islem_ekle(Gider(tutar, aciklama, kategori, tarih_str))
            except ValueError:
                print("❌ Hata: Tutar sayı olmalı!")

        elif secim == '3':
            yonetici.bakiye_goster()

        elif secim == '4':
            print("\n🤖 AI Modelleri Eğitiliyor ve Grafik Çiziliyor...")
            grafik_cizici.grafik_olustur()

        elif secim == '5':
            tip = input("Format (pdf / excel): ").lower()
            print(f"\n✅ {RaporFactory.rapor_uret(tip)}")

        elif secim == '6':
            print("Güle güle! 👋")
            break

        else:
            print("Geçersiz seçenek.")


if __name__ == "__main__":
    uygulamayi_baslat()