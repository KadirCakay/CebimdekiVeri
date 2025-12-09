import pandas as pd
import random
from datetime import datetime, timedelta


def veri_olustur():
    print("=" * 50)
    print("   KİŞİSELLEŞTİRİLMİŞ VERİ SETİ OLUŞTURUCU (V2 - STABİL)")
    print("   (Daha tutarlı tahminler için 2 yıllık veri üretir)")
    print("=" * 50)

    try:
        print("\nLütfen aylık ortalama giderlerini gir (Tahmini):")
        # Kullanıcıdan verileri alıyoruz
        kira = float(input("🏠 Kira/Yurt Giderin (TL): "))
        market = float(input("🛒 Ortalama Market (TL): "))
        ulasim = float(input("🚌 Ortalama Ulaşım (TL): "))
        fatura = float(input("💡 Ortalama Faturalar (TL): "))
        eglence = float(input("🎉 Eğlence/Sosyal (TL): "))
        maas = float(input("💰 Aylık Ortalama Gelirin (Burs/Maaş) (TL): "))
    except ValueError:
        print("Lütfen sadece sayı girin!")
        return

    # --- DEĞİŞİKLİK 1: 1 YIL YERİNE 2 YIL (730 GÜN) ---
    # Daha fazla veri = Daha akıllı yapay zeka
    gun_sayisi = 730
    baslangic_tarihi = datetime.now() - timedelta(days=gun_sayisi)
    veri_seti = []

    print(f"\n⏳ Geçmiş {int(gun_sayisi / 365)} yıl simüle ediliyor...")

    for i in range(gun_sayisi):
        gun = baslangic_tarihi + timedelta(days=i)

        # --- DEĞİŞİKLİK 2: ENFLASYON ETKİSİNİ KALDIRDIK/AZALTTIK ---
        # Eskiden her gün artan bir çarpan vardı. Şimdi "Rastgele Dalgalanma" var.
        # Yani bazen %10 fazla, bazen %10 az harcarsın ama sürekli artmaz.

        dalgalanma = random.uniform(0.90, 1.10)  # %10 aşağı veya yukarı oynasın

        # 1. GELİR (Her ayın 15'inde)
        if gun.day == 15:
            # Gelire hafif zam yapalım (Yılda bir kez %10) - Daha gerçekçi
            yil_farki = (datetime.now().year - gun.year)
            zam_orani = 1.0
            if yil_farki == 0: zam_orani = 1.10  # Bu yıl maaş biraz daha yüksek olsun

            veri_seti.append({
                "Tarih": gun.strftime("%Y-%m-%d"),
                "Kategori": "Maaş/Burs",
                "Tutar": int(maas * zam_orani),
                "Islem_Tipi": "Gelir"
            })

        # 2. SABİT GİDER (Kira - Her ayın 1'inde)
        if gun.day == 1:
            veri_seti.append({
                "Tarih": gun.strftime("%Y-%m-%d"),
                "Kategori": "Kira",
                "Tutar": int(kira),  # Kira genelde sabittir
                "Islem_Tipi": "Gider"
            })

        # 3. DEĞİŞKEN GİDERLER (Enflasyon yerine Dalgalanma kullanıyoruz)

        # Market: Ayda ortalama 8 kez
        if random.random() < (8 / 30):
            tutar = (market / 8) * dalgalanma
            veri_seti.append(
                {"Tarih": gun.strftime("%Y-%m-%d"), "Kategori": "Market", "Tutar": int(tutar), "Islem_Tipi": "Gider"})

        # Ulaşım: Ayda 20 kez
        if random.random() < (20 / 30):
            tutar = (ulasim / 20) * dalgalanma
            veri_seti.append(
                {"Tarih": gun.strftime("%Y-%m-%d"), "Kategori": "Ulaşım", "Tutar": int(tutar), "Islem_Tipi": "Gider"})

        # Fatura: Ayda 1 kez (Rastgele bir gün)
        if random.random() < (1 / 30):
            tutar = fatura * dalgalanma
            veri_seti.append(
                {"Tarih": gun.strftime("%Y-%m-%d"), "Kategori": "Fatura", "Tutar": int(tutar), "Islem_Tipi": "Gider"})

        # Eğlence: Haftada 1-2 kez
        if random.random() < (6 / 30):
            tutar = (eglence / 6) * random.uniform(0.5, 1.5)  # Eğlence çok değişken olabilir
            veri_seti.append(
                {"Tarih": gun.strftime("%Y-%m-%d"), "Kategori": "Eğlence", "Tutar": int(tutar), "Islem_Tipi": "Gider"})

    # Veriyi Kaydet
    df = pd.DataFrame(veri_seti)
    df.to_csv("butce_verisi.csv", index=False)
    print("\n✅ Veri seti başarıyla oluşturuldu! (Stabil Versiyon)")
    print("✅ Şimdi main.py'yi çalıştırıp 'Analiz' yapabilirsin.")


if __name__ == "__main__":
    veri_olustur()