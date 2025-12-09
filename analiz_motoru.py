import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import os


class TahminMotoru:
    def __init__(self, veri_yolu="butce_verisi.csv"):
        self.veri_yolu = veri_yolu

    def veri_getir(self):
        if not os.path.exists(self.veri_yolu):
            return None

        df = pd.read_csv(self.veri_yolu)
        df['Tarih'] = pd.to_datetime(df['Tarih'])
        return df

    def gelecek_tahmini_yap(self):

        df = self.veri_getir()
        if df is None: return None, None, None, None

        # Aylık Özet
        aylik_ozet = df.groupby([pd.Grouper(key='Tarih', freq='ME'), 'Islem_Tipi'])['Tutar'].sum().unstack().fillna(0)

        if 'Gelir' not in aylik_ozet.columns: aylik_ozet['Gelir'] = 0
        if 'Gider' not in aylik_ozet.columns: aylik_ozet['Gider'] = 0

        # --- YAPAY ZEKA MODELİ ---
        X = np.arange(len(aylik_ozet)).reshape(-1, 1)

        # Modelleri Eğit
        model_gelir = LinearRegression().fit(X, aylik_ozet['Gelir'].values)
        model_gider = LinearRegression().fit(X, aylik_ozet['Gider'].values)

        # Gelecek Ayı Tahmin Et
        gelecek_index = np.array([[len(aylik_ozet)]])
        tahmin_gelir = max(0, model_gelir.predict(gelecek_index)[0])
        tahmin_gider = max(0, model_gider.predict(gelecek_index)[0])

        return aylik_ozet, tahmin_gelir, tahmin_gider, df