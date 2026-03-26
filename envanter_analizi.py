import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# --- 1. VERİTABANI VE ÖRNEK VERİ HAZIRLAMA ---
def veritabani_hazirla(db_adi="envanter_sistemi.db"):
    """
    Sistem için gerekli SQLite veritabanını oluşturur ve 
    test amaçlı örnek verileri içeri aktarır.
    """
    with sqlite3.connect(db_adi) as baglanti:
        imlec = baglanti.cursor()
        
        # Temiz bir başlangıç için tabloyu sıfırla
        imlec.execute("DROP TABLE IF EXISTS envanter")
        imlec.execute("""
            CREATE TABLE envanter (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                urun_adi TEXT NOT NULL,
                stok_miktari INTEGER,
                birim_fiyat REAL,
                kategori TEXT
            )
        """)
        
        # Genel İşletme Veri Seti
        ornek_veriler = [
            ('Endüstriyel Motor V1', 45, 1550.0, 'Üretim'),
            ('Hassas Sensör Grubu', 12, 620.0, 'Elektronik'),
            ('Yalıtım Paneli (Standart)', 200, 45.5, 'Sarf Malzeme'),
            ('Kontrol Ünitesi (Ar-Ge)', 8, 3100.0, 'Elektronik'),
            ('Sızdırmazlık Fitili 5m', 550, 12.0, 'Sarf Malzeme'),
            ('Dijital Gösterge Modülü', 25, 280.0, 'Elektronik')
        ]
        
        imlec.executemany(
            "INSERT INTO envanter (urun_adi, stok_miktari, birim_fiyat, kategori) VALUES (?, ?, ?, ?)", 
            ornek_veriler
        )
        baglanti.commit()
    print(f"✅ Sistem Başlatıldı: '{db_adi}' başarıyla oluşturuldu.")

# --- 2. VERİ ANALİZİ, RAPORLAMA VE GÖRSELLEŞTİRME ---
def analiz_ve_raporlama(db_adi="envanter_sistemi.db", kritik_esik=20):
    """
    Veritabanındaki verileri analiz eder, kritik stokları belirler,
    Excel raporu oluşturur ve verileri grafik olarak sunar.
    """
    with sqlite3.connect(db_adi) as baglanti:
        # Veriyi Pandas DataFrame'e aktar
        df = pd.read_sql_query("SELECT * FROM envanter", baglanti)
        
        print("\n📊 GÜNCEL STOK DURUMU:")
        # Terminalde düzgün görünmesi için to_string kullanıldı
        print(df.to_string(index=False)) 
        
        # Kritik Stok Algoritması
        kritik_df = df[df['stok_miktari'] < kritik_esik]
        
        if not kritik_df.empty:
            print(f"\n⚠️ KRİTİK SEVİYE UYARISI ({len(kritik_df)} Ürün):")
            for _, satir in kritik_df.iterrows():
                print(f"   -> [ACİL TEDARİK] {satir['urun_adi']}: Sadece {satir['stok_miktari']} adet kaldı.")
        
        # Excel Raporu Oluşturma
        excel_adi = "Genel_Envanter_Raporu.xlsx"
        df.to_excel(excel_adi, index=False)
        print(f"\n📂 Yönetim raporu '{excel_adi}' adıyla oluşturuldu.")
        
        # VERİ GÖRSELLEŞTİRME
        plt.style.use('ggplot') # Profesyonel görünüm için stil ayarı
        plt.figure(figsize=(10, 6))
        
        # Renklendirme Mantığı: Kritik ürünler kırmızı (#e74c3c), diğerleri mavi (#3498db)
        renkler = ['#e74c3c' if m < kritik_esik else '#3498db' for m in df['stok_miktari']]
        
        bars = plt.bar(df['urun_adi'], df['stok_miktari'], color=renkler, edgecolor='black', alpha=0.8)
        plt.axhline(y=kritik_esik, color='red', linestyle='--', label=f'Kritik Eşik ({kritik_esik})')
        
        plt.title('İşletme Envanter Seviye Analizi', fontsize=14, fontweight='bold')
        plt.ylabel('Stok Miktarı (Adet)')
        plt.xlabel('Ürün Adı')
        plt.xticks(rotation=30, ha='right')
        plt.legend()
        plt.grid(axis='y', linestyle=':', alpha=0.7)
        
        # Sütunların üzerine miktar bilgisini ekle
        for bar in bars:
            yval = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2, yval + 5, int(yval), ha='center', va='bottom', fontweight='bold')

        plt.tight_layout()
        print("\n📈 Grafik oluşturuldu. Kapatmak için grafik penceresini onaylayın.")
        plt.show()

# --- ANA PROGRAM AKIŞI ---
if __name__ == "__main__":
    try:
        veritabani_hazirla()
        analiz_ve_raporlama()
    except Exception as e:
        print(f"❌ Bir hata oluştu: {e}")
