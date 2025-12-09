import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from analiz_motoru import TahminMotoru


def grafik_olustur():
    motor = TahminMotoru()
    aylik_ozet, tah_gelir, tah_gider, ham_veri = motor.gelecek_tahmini_yap()

    if aylik_ozet is None:
        print("❌ Veri yok, grafik çizilemedi.")
        return

    # Tarih Bilgileri
    son_tarih = aylik_ozet.index[-1]
    gelecek_tarih = son_tarih + pd.DateOffset(months=1)

    # --- ÇİZİM ---
    plt.figure(figsize=(16, 8))

    # SOL GRAFİK: Gider Pastası
    plt.subplot(1, 2, 1)
    sadece_giderler = ham_veri[ham_veri['Islem_Tipi'] == 'Gider']
    kategori_toplam = sadece_giderler.groupby("Kategori")["Tutar"].sum()

    if not kategori_toplam.empty:
        explode = [0.05] * len(kategori_toplam)
        colors = sns.color_palette("pastel")[0:len(kategori_toplam)]
        plt.pie(kategori_toplam, labels=kategori_toplam.index, autopct='%1.1f%%',
                startangle=140, explode=explode, shadow=True, colors=colors)
        plt.title("Harcama Dağılımı", fontsize=13)
    else:
        plt.text(0.5, 0.5, "Henüz Gider Verisi Yok", ha='center')

    # SAĞ GRAFİK: Trend ve AI Tahmini
    plt.subplot(1, 2, 2)

    # Gerçek Veriler
    plt.plot(aylik_ozet.index, aylik_ozet['Gelir'], marker='o', color='green', linewidth=2, label='Gerçekleşen Gelir')
    plt.plot(aylik_ozet.index, aylik_ozet['Gider'], marker='o', color='red', linewidth=2, label='Gerçekleşen Gider')

    # AI Tahmin Çizgisi
    plt.plot([son_tarih, gelecek_tarih], [aylik_ozet['Gelir'].iloc[-1], tah_gelir],
             color='green', linestyle='--', marker='*', markersize=12, label='AI Tahmini')

    plt.plot([son_tarih, gelecek_tarih], [aylik_ozet['Gider'].iloc[-1], tah_gider],
             color='red', linestyle='--', marker='*', markersize=12, label='AI Tahmini')

    # Etiket
    plt.annotate(f"AI Gider Tahmini:\n{int(tah_gider)} TL",
                 (gelecek_tarih, tah_gider),
                 textcoords="offset points", xytext=(15, 0), ha='left', color='red', fontweight='bold',
                 bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="red", lw=2))

    plt.fill_between(aylik_ozet.index, aylik_ozet['Gelir'], aylik_ozet['Gider'],
                     where=(aylik_ozet['Gelir'] >= aylik_ozet['Gider']),
                     interpolate=True, color='green', alpha=0.05)

    plt.fill_between(aylik_ozet.index, aylik_ozet['Gelir'], aylik_ozet['Gider'],
                     where=(aylik_ozet['Gelir'] < aylik_ozet['Gider']),
                     interpolate=True, color='red', alpha=0.05)

    plt.title("Finansal Trend ve Yapay Zeka Analizi", fontsize=14)
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.savefig("sunum_grafikleri.png")

    print(f"\n✅ Analiz ve Çizim Tamamlandı.")
    print(f"🔮 Gelecek Ay Tahmini -> Gelir: {int(tah_gelir)} TL | Gider: {int(tah_gider)} TL")