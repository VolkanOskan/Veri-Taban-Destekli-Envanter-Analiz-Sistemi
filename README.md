# 📦 Veri Tabanı Destekli Envanter Analiz Sistemi

Bu proje, işletmelerin stok süreçlerini dijitalleştirmek, veritabanı üzerinden takibini yapmak ve envanter durumunu profesyonel grafiklerle analiz etmek amacıyla geliştirilmiş bir **Python** uygulamasıdır.

## 🚀 Projenin Amacı
İşletmelerin elindeki stokların yönetimini kolaylaştırmak, kritik seviyedeki ürünler için otomatik uyarı sistemi oluşturmak ve verileri hem görsel (grafik) hem de dökümantasyon (Excel) bazlı raporlamaktır.

## ✨ Temel Özellikler
- **SQLite Entegrasyonu:** Veriler hafif ve taşınabilir bir SQL veritabanında (`.db`) güvenle saklanır.
- **Kritik Stok Algoritması:** Stok miktarı 20 adetin altına düşen ürünler sistem tarafından otomatik olarak tespit edilir ve terminalde raporlanır.
- **Veri Analizi (Pandas):** Envanter verileri üzerinden hızlı ve etkili veri işleme yapılır.
- **Görselleştirme (Matplotlib):** Stok seviyeleri, kritik eşiği gösteren dinamik ve renk kodlu grafiklerle sunulur.
- **Excel Raporlama:** Tüm envanter verileri tek tıkla `Genel_Envanter_Raporu.xlsx` dosyası olarak dışa aktarılır.

## 🛠️ Kullanılan Teknolojiler
* **Programlama Dili:** Python
* **Veritabanı:** SQLite3
* **Veri İşleme:** Pandas
* **Görselleştirme:** Matplotlib
* **Raporlama:** Openpyxl

## 📋 Kurulum ve Kullanım
1. **Gerekli kütüphaneleri yükleyin:**
   ```bash
   pip install pandas matplotlib openpyxl
